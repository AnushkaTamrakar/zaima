from datetime import datetime, date, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.orm import Session
from ..models.user import User
from ..models.contact import Contact
from ..models.checkin import Checkin
from ..services.mail import send_alert_email
from ..config import settings
from .database import SessionLocal


def check_missed_checkins():
    """检查所有用户的签到情况，对连续多日未签到的用户发送通知"""
    db = SessionLocal()
    try:
        # 获取当前日期
        today = date.today()
        max_days = settings.max_consecutive_days
        
        # 查询所有用户
        users = db.query(User).all()
        
        for user in users:
            # 获取用户的紧急联系人
            contact = db.query(Contact).filter(Contact.user_id == user.id).first()
            if not contact:
                continue  # 没有设置紧急联系人，跳过
            
            # 获取用户最近的签到记录
            latest_checkin = db.query(Checkin).filter(
                Checkin.user_id == user.id
            ).order_by(Checkin.checkin_date.desc()).first()
            
            if not latest_checkin:
                # 从未签到过，跳过
                continue
            
            # 计算连续未签到天数
            days_since_last_checkin = (today - latest_checkin.checkin_date).days
            
            # 如果连续未签到天数超过阈值，发送通知
            if days_since_last_checkin > max_days:
                send_alert_email(
                    contact_name=contact.name,
                    contact_email=contact.email,
                    consecutive_days=days_since_last_checkin
                )
    finally:
        db.close()


def setup_cron_jobs(app):
    """设置定时任务"""
    # 创建后台调度器
    scheduler = BackgroundScheduler()
    
    # 添加定时任务：每天凌晨1点执行
    scheduler.add_job(
        func=check_missed_checkins,
        trigger=CronTrigger(hour=1, minute=0),
        id="check_missed_checkins",
        name="检查未签到用户并发送通知",
        replace_existing=True
    )
    
    # 启动调度器
    scheduler.start()
    
    print("定时任务已启动：每天凌晨1点检查未签到用户")
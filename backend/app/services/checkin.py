from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.checkin import Checkin
from ..models.user import User


def checkin_today(db: Session, user: User) -> bool:
    """检查用户今天是否已签到"""
    today = date.today()
    return db.query(Checkin).filter(
        Checkin.user_id == user.id,
        Checkin.checkin_date == today
    ).first() is not None


def create_checkin(db: Session, user: User) -> Checkin:
    """创建签到记录"""
    today = date.today()
    checkin = Checkin(user_id=user.id, checkin_date=today)
    db.add(checkin)
    db.commit()
    db.refresh(checkin)
    return checkin


def get_consecutive_days(db: Session, user: User) -> int:
    """计算用户连续签到天数"""
    today = date.today()
    consecutive_days = 0
    
    # 从今天开始往前查找连续签到记录
    for i in range(365):  # 最多检查一年
        check_date = today - timedelta(days=i)
        
        # 检查该日期是否有签到记录
        has_checkin = db.query(Checkin).filter(
            Checkin.user_id == user.id,
            Checkin.checkin_date == check_date
        ).first() is not None
        
        if has_checkin:
            consecutive_days += 1
        else:
            break  # 连续签到中断
    
    return consecutive_days


def get_checkin_status(db: Session, user: User):
    """获取用户签到状态"""
    today = date.today()
    has_checked_in = checkin_today(db, user)
    consecutive_days = get_consecutive_days(db, user)
    
    # 获取最近的签到日期
    latest_checkin = db.query(Checkin).filter(
        Checkin.user_id == user.id
    ).order_by(Checkin.checkin_date.desc()).first()
    
    checkin_date = latest_checkin.checkin_date if latest_checkin else None
    
    return {
        "has_checked_in_today": has_checked_in,
        "checkin_date": checkin_date,
        "consecutive_days": consecutive_days
    }


def get_last_checkin_date(db: Session, user: User) -> date:
    """获取用户最后一次签到日期"""
    last_checkin = db.query(Checkin).filter(
        Checkin.user_id == user.id
    ).order_by(Checkin.checkin_date.desc()).first()
    
    return last_checkin.checkin_date if last_checkin else None
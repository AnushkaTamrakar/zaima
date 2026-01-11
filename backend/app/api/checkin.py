from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date
from ..schemas.checkin import CheckinResponse, CheckinStatusResponse
from ..services.checkin import (
    checkin_today,
    create_checkin,
    get_consecutive_days,
    get_checkin_status
)
from ..utils.database import get_db
from ..api.deps import get_current_user
from ..models.user import User

router = APIRouter()


@router.post("/", response_model=CheckinResponse, summary="用户签到")
def user_checkin(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    用户签到接口：
    - 检查用户今天是否已签到
    - 如果未签到，创建签到记录
    - 返回签到结果和连续签到天数
    """
    # 检查今天是否已签到
    if checkin_today(db, current_user):
        consecutive_days = get_consecutive_days(db, current_user)
        return CheckinResponse(
            message="您今天已经签到过了",
            checkin_date=date.today(),
            is_success=False,
            consecutive_days=consecutive_days
        )
    
    # 创建签到记录
    checkin = create_checkin(db, current_user)
    consecutive_days = get_consecutive_days(db, current_user)
    
    return CheckinResponse(
        message="签到成功",
        checkin_date=checkin.checkin_date,
        is_success=True,
        consecutive_days=consecutive_days
    )


@router.get("/status", response_model=CheckinStatusResponse, summary="获取签到状态")
def get_status(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    获取用户签到状态：
    - 今天是否已签到
    - 最近一次签到日期
    - 连续签到天数
    """
    status_data = get_checkin_status(db, current_user)
    return CheckinStatusResponse(**status_data)
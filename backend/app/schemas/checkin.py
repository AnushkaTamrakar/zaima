from pydantic import BaseModel
from datetime import date
from typing import Optional


class CheckinResponse(BaseModel):
    """签到响应模型"""
    message: str
    checkin_date: date
    is_success: bool
    consecutive_days: int
    
    class Config:
        from_attributes = True


class CheckinStatusResponse(BaseModel):
    """签到状态响应模型"""
    has_checked_in_today: bool
    checkin_date: Optional[date] = None
    consecutive_days: int
    
    class Config:
        from_attributes = True
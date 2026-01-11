from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..utils.security import verify_token
from ..utils.database import get_db
from ..models.user import User

# 创建OAuth2密码承载令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """获取当前用户"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # 验证令牌并获取设备ID
    device_id = verify_token(token, credentials_exception)
    
    # 查找用户
    user = db.query(User).filter(User.device_id == device_id).first()
    if user is None:
        raise credentials_exception
    
    return user
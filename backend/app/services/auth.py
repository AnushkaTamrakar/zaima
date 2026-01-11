from sqlalchemy.orm import Session
from ..models.user import User
from ..utils.security import create_access_token


def authenticate_user(db: Session, device_id: str):
    """验证用户并返回用户对象"""
    # 查找设备ID对应的用户
    user = db.query(User).filter(User.device_id == device_id).first()
    
    # 如果用户不存在，创建新用户
    if not user:
        user = User(device_id=device_id)
        db.add(user)
        db.commit()
        db.refresh(user)
    
    return user


def create_user_token(user: User):
    """为用户创建访问令牌"""
    access_token = create_access_token(
        data={"sub": user.device_id}
    )
    return access_token
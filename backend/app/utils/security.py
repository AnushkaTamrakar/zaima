from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from ..config import settings

# 创建密码上下文（虽然我们不需要密码，但保留此功能）
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta = None):
    """生成访问令牌"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    """验证令牌"""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        device_id: str = payload.get("sub")
        if device_id is None:
            raise credentials_exception
        return device_id
    except JWTError:
        raise credentials_exception
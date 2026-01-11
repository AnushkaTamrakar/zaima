from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.auth import LoginRequest, Token
from ..services.auth import authenticate_user, create_user_token
from ..utils.database import get_db

router = APIRouter()


@router.post("/login", response_model=Token, summary="无感知登录")
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    """
    无感知登录接口：
    - 接收设备ID
    - 如果设备ID不存在，创建新用户
    - 生成并返回JWT令牌
    """
    # 验证用户并获取用户对象
    user = authenticate_user(db, login_request.device_id)
    
    # 创建访问令牌
    access_token = create_user_token(user)
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
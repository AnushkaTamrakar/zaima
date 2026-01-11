from pydantic import BaseModel, EmailStr
from typing import Optional


class ContactCreate(BaseModel):
    """创建联系人请求模型"""
    name: str
    email: EmailStr


class ContactUpdate(BaseModel):
    """更新联系人请求模型"""
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class ContactResponse(BaseModel):
    """联系人响应模型"""
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True
from sqlalchemy.orm import Session
from ..models.contact import Contact
from ..models.user import User
from ..schemas.contact import ContactCreate, ContactUpdate


def get_user_contact(db: Session, user: User) -> Contact:
    """获取用户的紧急联系人"""
    return db.query(Contact).filter(Contact.user_id == user.id).first()


def create_or_update_contact(
    db: Session, 
    user: User, 
    contact_data: ContactCreate
) -> Contact:
    """创建或更新用户的紧急联系人"""
    # 查找用户的紧急联系人
    contact = get_user_contact(db, user)
    
    if contact:
        # 更新现有联系人
        contact.name = contact_data.name
        contact.email = contact_data.email
        db.commit()
        db.refresh(contact)
    else:
        # 创建新联系人
        contact = Contact(
            user_id=user.id,
            name=contact_data.name,
            email=contact_data.email
        )
        db.add(contact)
        db.commit()
        db.refresh(contact)
    
    return contact


def update_contact_partial(
    db: Session, 
    user: User, 
    contact_update: ContactUpdate
) -> Contact:
    """部分更新用户的紧急联系人"""
    contact = get_user_contact(db, user)
    
    if not contact:
        return None
    
    # 更新提供的字段
    update_data = contact_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(contact, field, value)
    
    db.commit()
    db.refresh(contact)
    return contact


def delete_contact(db: Session, user: User) -> bool:
    """删除用户的紧急联系人"""
    contact = get_user_contact(db, user)
    
    if not contact:
        return False
    
    db.delete(contact)
    db.commit()
    return True
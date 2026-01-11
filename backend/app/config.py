from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # 应用配置
    app_name: str = "SoloSafe"
    app_version: str = "1.0.0"
    debug: bool = True

    # 数据库配置
    database_url: str = "sqlite:///./solo_safe.db"

    # JWT配置
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # 邮件配置
    mail_server: str = "smtp.gmail.com"
    mail_port: int = 587
    mail_username: str = "your-email@gmail.com"
    mail_password: str = "your-email-password"
    mail_from: str = "your-email@gmail.com"
    mail_use_tls: bool = True
    mail_use_ssl: bool = False

    # 签到配置
    max_consecutive_days: int = 3

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
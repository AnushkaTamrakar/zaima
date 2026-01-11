from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .api import auth, checkin, contact
from .utils import database
from .utils.cron import setup_cron_jobs

# 创建数据库表
database.Base.metadata.create_all(bind=database.engine)

# 创建FastAPI应用
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该指定允许的源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(checkin.router, prefix="/api/checkin", tags=["checkin"])
app.include_router(contact.router, prefix="/api/contact", tags=["contact"])

# 配置定时任务
setup_cron_jobs(app)


@app.get("/")
def read_root():
    """根路径"""
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "message": "欢迎使用zaima安全工具API"
    }
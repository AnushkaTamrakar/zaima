import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..config import settings


def send_alert_email(contact_name: str, contact_email: str, consecutive_days: int):
    """
    发送异常未签到通知邮件
    
    Args:
        contact_name: 联系人姓名
        contact_email: 联系人邮箱
        consecutive_days: 连续未签到天数
    
    Returns:
        bool: 邮件发送是否成功
    """
    try:
        # 创建邮件消息
        msg = MIMEMultipart()
        msg["From"] = settings.mail_from
        msg["To"] = contact_email
        msg["Subject"] = "紧急通知：您的联系人连续多日未签到"
        
        # 邮件正文模板
        html_content = f"""
        <html>
        <body>
            <h2>紧急通知</h2>
            <p>亲爱的 {contact_name}：</p>
            <p>您的联系人已连续 <strong>{consecutive_days} 天</strong> 未在 <strong>{settings.app_name}</strong> 应用中签到。</p>
            <p>请尽快联系您的家人或朋友，确认他们的身体状况和安全。</p>
            <p>这是一条自动发送的通知，请勿直接回复。</p>
            <br>
            <p>此致</p>
            <p>{settings.app_name} 团队</p>
        </body>
        </html>
        """
        
        # 附件正文到邮件
        msg.attach(MIMEText(html_content, "html"))
        
        # 连接到邮件服务器并发送邮件
        if settings.mail_use_ssl:
            server = smtplib.SMTP_SSL(settings.mail_server, settings.mail_port)
        else:
            server = smtplib.SMTP(settings.mail_server, settings.mail_port)
            if settings.mail_use_tls:
                server.starttls()
        
        # 登录邮箱
        server.login(settings.mail_username, settings.mail_password)
        
        # 发送邮件
        server.send_message(msg)
        
        # 关闭连接
        server.quit()
        
        return True
    except Exception as e:
        print(f"邮件发送失败：{str(e)}")
        return False
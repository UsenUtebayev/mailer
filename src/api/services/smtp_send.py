import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
from starlette.responses import JSONResponse

from src.models.message import Message

logger = logging.getLogger(__name__)


def smtp_send(msg: Message):
    """Сервисная функция для отправки сообщения"""
    load_dotenv()
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMPT_PORT'))
    smtp_username = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMPT_PASSWORD')

    email_message = MIMEMultipart()
    email_message["From"] = smtp_username
    email_message["To"] = msg.to
    email_message["Subject"] = msg.subject
    email_message.attach(MIMEText(msg.message, "plain"))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(email_message)
        server.quit()
        logger.info(f'mail sended to {msg.to} succesfully')
        return JSONResponse(status_code=200, content={"message": "Email send succesfully"})
    except smtplib.SMTPAuthenticationError as e:
        return JSONResponse(status_code=200, content={"message": f"Failed to send email: {str(e)}"})

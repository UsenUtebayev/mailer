import os
import smtplib

from dotenv import load_dotenv


def test_smtp_connection():
    """Проверка соединения с SMTP сервера"""
    load_dotenv()
    smtp_host = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMPT_PORT"))
    try:
        smtp_obj = smtplib.SMTP(smtp_host, smtp_port)
        response = smtp_obj.ehlo()
        smtp_obj.quit()
        assert response[0] == 250
    except Exception as e:
        print("Ошибка при проверке статуса SMTP-сервера:", str(e))
        return False

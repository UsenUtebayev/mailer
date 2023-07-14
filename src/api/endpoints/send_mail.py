import logging
from fastapi import APIRouter
from email_validator import validate_email, EmailNotValidError

from starlette.responses import JSONResponse
from ..services.smtp_send import smtp_send
from src.models.message import Message

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/send_email")
async def send_email(msg: Message) -> JSONResponse:
    """POST запрос для отправки сообщения через SMTP сервер"""
    try:
        to = validate_email(msg.to).original
    except EmailNotValidError as e:
        logger.error(f'Email valid error {str(e)}')
        return JSONResponse(status_code=422, content={"message": f"Failed to send email: {str(e)}"})

    return smtp_send(msg)


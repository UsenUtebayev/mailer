import logging

from fastapi import FastAPI

from src.api.endpoints import send_mail

logging.basicConfig(level=logging.DEBUG)
app = FastAPI()

app.include_router(send_mail.router)

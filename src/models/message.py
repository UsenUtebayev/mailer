from dataclasses import Field

from pydantic import BaseModel, constr


class Message(BaseModel):
    to: str
    subject: constr(min_length=1, max_length=2048)
    message: constr(min_length=1)

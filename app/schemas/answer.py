# answer.py

from pydantic import BaseModel, UUID4
from datetime import datetime


class AnswerBase(BaseModel):
    text: str


class AnswerCreate(AnswerBase):
    user_id: UUID4


class AnswerOut(AnswerBase):
    id: int
    question_id: int
    user_id: UUID4
    created_at: datetime

    class Config:
        orm_mode = True

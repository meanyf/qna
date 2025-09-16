# question.py

from pydantic import BaseModel
from datetime import datetime

from app.schemas.answer import AnswerOut


class QuestionBase(BaseModel):
    text: str


class QuestionCreate(QuestionBase):
    pass


class QuestionOut(BaseModel):
    id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True


class QuestionAndAnswersOut(QuestionOut):
    answers: list[AnswerOut] = []

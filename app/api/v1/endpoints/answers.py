# answers.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.answer import AnswerOut, AnswerCreate
from app.services import answers_service

answers_router = APIRouter(prefix="/answers", tags=["answers"])
question_answers_router = APIRouter(
    prefix="/questions/{question_id}/answers", tags=["answers"]
)

@answers_router.get("/{answer_id}", response_model=AnswerOut)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    return answers_service.get_answer(db, answer_id)


@answers_router.delete("/{answer_id}")
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    answers_service.delete_answer(db, answer_id)
    return {"ok": True}


@question_answers_router.post("/", response_model=AnswerOut)
def create_answer(
    question_id: int, payload: AnswerCreate, db: Session = Depends(get_db)
):
    return answers_service.create_answer(
        db, question_id=question_id, user_id=payload.user_id, text=payload.text
    )

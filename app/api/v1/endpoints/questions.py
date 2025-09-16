# questions.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.question import QuestionOut, QuestionCreate, QuestionAndAnswersOut

from app.services import questions_service

questions_router = APIRouter(prefix="/questions", tags=["questions"])


@questions_router.get("/", response_model=list[QuestionOut])
def list_questions(db: Session = Depends(get_db)):
    return questions_service.list_questions(db)


@questions_router.post("/", response_model=QuestionOut)
def create_question(payload: QuestionCreate, db: Session = Depends(get_db)):
    return questions_service.create_question(db, text=payload.text)


@questions_router.get("/{question_id}", response_model=QuestionAndAnswersOut)
def read_question(question_id: int, db: Session = Depends(get_db)):
    return questions_service.get_question(db, question_id)


@questions_router.delete("/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    questions_service.delete_question(db, question_id)
    return {"ok": True}

# questions_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.db import crud
from app.db.models import Question


def create_question(db: Session, text: str) -> Question:
    """Создать новый вопрос."""
    try:
        question = crud.create_question(db, text=text)
        db.commit()
        db.refresh(question)
        return question
    except Exception:
        db.rollback()
        raise


def get_question(db: Session, question_id: int) -> Question:
    """Получить вопрос по ID или вернуть 404."""
    question = crud.get_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


def list_questions(db: Session) -> list[Question]:
    """Список вопросов."""
    return crud.list_questions(db)


def delete_question(db: Session, question_id: int) -> None:
    """Удалить вопрос (с каскадным удалением ответов)."""
    question = crud.get_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    crud.delete_question(db, question)
    db.commit()

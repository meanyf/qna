# answers_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.db import crud
from app.db.models import Answer


def create_answer(db: Session, question_id: int, user_id, text: str) -> Answer:
    """Создать новый ответ для вопроса."""
    # Проверяем, что вопрос существует
    question = crud.get_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=400, detail="Question does not exist")

    try:
        answer = crud.create_answer(db, question=question, user_id=user_id, text=text)
        db.commit()
        db.refresh(answer)
        return answer
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="DB integrity error")


def get_answer(db: Session, answer_id: int) -> Answer:
    """Получить ответ по ID или вернуть 404."""
    answer = crud.get_answer(db, answer_id)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer


def update_answer(
    db: Session, answer_id: int, update_data: dict, current_user_id
) -> Answer:
    """Обновить ответ (без возможности смены question_id)."""
    answer = crud.get_answer(db, answer_id)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")

    # Нельзя менять question_id напрямую
    if "question_id" in update_data:
        raise HTTPException(status_code=400, detail="Changing question_id is forbidden")

    # Проверка прав: редактировать может только автор
    if str(answer.user_id) != str(current_user_id):
        raise HTTPException(status_code=403, detail="Not allowed")

    crud.update_answer(db, answer, **update_data)
    db.commit()
    db.refresh(answer)
    return answer


def delete_answer(db: Session, answer_id: int, current_user_id) -> None:
    """Удалить ответ (только автор может)."""
    answer = crud.get_answer(db, answer_id)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")

    if str(answer.user_id) != str(current_user_id):
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(answer)
    db.commit()

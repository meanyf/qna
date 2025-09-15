# crud.py

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.models import Question, Answer


# --- Question helpers ---
def get_question(db: Session, question_id: int) -> Question | None:
    return db.execute(
        select(Question).where(Question.id == question_id)
    ).scalar_one_or_none()


def create_question(db: Session, *, text: str) -> Question:
    question = Question(text=text)
    db.add(question)
    db.flush()  # чтобы получить id до commit
    return question


def list_questions(db: Session, skip: int = 0, limit: int = 100) -> list[Question]:
    return db.execute(select(Question).offset(skip).limit(limit)).scalars().all()


def update_question(db: Session, question: Question, *, text: str) -> Question:
    question.text = text
    db.flush()
    return question


def delete_question(db: Session, question: Question) -> None:
    db.delete(question)
    db.flush()


# --- Answer helpers ---
def create_answer(db: Session, *, question: Question, user_id, text) -> Answer:
    answer = Answer(question=question, user_id=user_id, text=text)
    db.add(answer)
    db.flush()  # чтобы получить id до commit
    return answer


def get_answer(db: Session, answer_id: int) -> Answer | None:
    return db.execute(select(Answer).where(Answer.id == answer_id)).scalar_one_or_none()


def update_answer(db: Session, answer: Answer, **fields) -> Answer:
    # никак не трогаем question_id здесь — это ответственность сервиса
    for k, v in fields.items():
        setattr(answer, k, v)
    db.flush()
    return answer

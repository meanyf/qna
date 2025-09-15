# models.py

# v err.py

import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(
        Integer, primary_key=True, autoincrement=True
    )  # Автоинкрементируемый PK для вопроса
    text = Column(Text, nullable=False)  # Текст вопроса (не может быть пустым)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # Дата создания вопроса

    # Связь с таблицей Answer
    answers = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan",
        passive_deletes=True,  # если используете ondelete на FK
    )


class Answer(Base):
    __tablename__ = "answers"

    id = Column(
        Integer, primary_key=True, autoincrement=True
    )  # Автоинкрементируемый PK для ответа

    question_id = Column(
        Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False
    )  # Внешний ключ на Question

    user_id = Column(UUID(as_uuid=True), nullable=False)  # UUID пользователя
    text = Column(Text, nullable=False)  # Текст ответа
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # Дата создания ответа

    # Связь с таблицей Question
    question = relationship("Question", back_populates="answers")

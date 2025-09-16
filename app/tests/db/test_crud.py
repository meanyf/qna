# test_crud.py

import pytest
from unittest.mock import MagicMock
from app.db.models import Question
from app.db.crud import list_questions
from sqlalchemy.orm import Session


# Мокируем сессию базы данных
@pytest.fixture
def mock_db_session():
    mock_session = MagicMock(spec=Session)  # Создаем мок-сессию
    # Мокируем выполнение запроса select
    mock_session.execute.return_value.scalars.return_value.all.return_value = [
        Question(id=1, text="What is your name?", created_at="2023-01-01T00:00:00")
    ]
    return mock_session


def test_list_questions(mock_db_session):
    # Вызов функции с мок-сессией
    questions = list_questions(mock_db_session)

    # Проверка, что результат — это список
    assert isinstance(questions, list)

    # Проверка, что в списке хотя бы один вопрос
    assert len(questions) > 0

    # Проверка содержимого первого вопроса
    question = questions[0]
    assert question.id == 1
    assert question.text == "What is your name?"
    assert question.created_at == "2023-01-01T00:00:00"

    # Проверка типа вопроса (должен быть экземпляр модели Question)
    assert isinstance(question, Question)

# test_answers.py

from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)


def test_get_questions():
    response = client.get("/api/v1/questions/")

    # Проверяем, что статус код 200
    assert response.status_code == 200

    # Получаем данные из ответа
    questions = response.json()

    # Проверяем, что ответ — это список
    assert isinstance(questions, list)

    # Если список не пуст, проверяем его содержимое
    if len(questions) > 0:
        # Проверяем, что каждый элемент соответствует модели QuestionOut
        for question in questions:
            # Проверка наличия обязательных полей
            assert "id" in question
            assert "text" in question
            assert "created_at" in question

            # Проверка типов данных
            assert isinstance(question["id"], int)
            assert isinstance(question["text"], str)

            # Проверка формата даты (проверяем, что created_at — валидная дата)
            try:
                datetime.fromisoformat(question["created_at"])
            except ValueError:
                assert (
                    False
                ), f"created_at for question {question['id']} is not in a valid datetime format"
    else:
        # Если список пуст, то можно добавить проверку на это:
        assert questions == []  # Проверяем, что возвращается пустой список

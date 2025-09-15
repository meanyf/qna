# main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.questions_service import create_question
from pydantic import BaseModel

app = FastAPI()


# Модель для данных запроса
class QuestionRequest(BaseModel):
    text: str


@app.post("/questions/")
def post_answer(question: QuestionRequest, db: Session = Depends(get_db)):
    question = create_question(db, question.text)  # Создаем вопрос с текстом
    return {"id": question.id, "text": question.text}

# api.py

from fastapi import APIRouter

from .endpoints.questions import questions_router
from .endpoints.answers import answers_router, question_answers_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(questions_router)
api_router.include_router(question_answers_router)
api_router.include_router(answers_router)

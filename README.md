# API для вопросов и ответов на FastAPI + PostgreSQL

## 1. Запуск 
```bash
docker-compose up --build
```

Приложение будет доступно по адресу:
http://localhost:8000

Документация API:
Swagger UI: http://localhost:8000/docs

## 2. Тесты
```bash
python -m pytest
```

## 2. Структура проекта
```
qna
├──alembic
│   ├──versions
│   │   └──09f3a35aa0df_create_questions_and_answers_tables.py
│   ├──env.py
│   ├──README
│   └──script.py.mako
├──app
│   ├──api
│   │   ├──v1
│   │   │   ├──endpoints
│   │   │   │   ├──__init__.py
│   │   │   │   ├──answers.py
│   │   │   │   └──questions.py
│   │   │   ├──__init__.py
│   │   │   └──api.py
│   │   ├──__init__.py
│   │   └──deps.py
│   ├──core
│   │   ├──__init__.py
│   │   └──config.py
│   ├──db
│   │   ├──__init__.py
│   │   ├──base.py
│   │   ├──crud.py
│   │   ├──models.py
│   │   └──session.py
│   ├──schemas
│   │   ├──__init__.py
│   │   ├──answer.py
│   │   └──question.py
│   ├──services
│   │   ├──answers_service.py
│   │   └──questions_service.py
│   ├──tests
│   │   ├──api
│   │   │   └──test_answers.py
│   │   └──db
│   │   │   └──test_crud.py
│   ├──__init__.py
│   └──main.py
├──alembic.ini
├──docker-compose.yml
├──Dockerfile
├──README.md
├──requirements.txt
├──structure.txt
└──.gitignore
```

# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .docker_utils import is_container_running

# Настройки БД
dbname = "qna_db"
user = "postgres"
password = "postgres"
host = "localhost"
port = 5435

# Определяем хост в зависимости от контейнеров
db_is_running = is_container_running("postgres15")
app_is_running = is_container_running("qna-fastapi")

if db_is_running and app_is_running:
    host = "postgres15"
elif db_is_running and not app_is_running:
    host = "localhost"
elif not db_is_running and app_is_running:
    host = "host.docker.internal" if host.lower() == "localhost" else host

# Строка подключения для SQLAlchemy
DATABASE_URL = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{dbname}"

# Создаём движок и фабрику сессий
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Базовый класс для моделей
Base = declarative_base()


# Dependency для FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# config.py
from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "QnA App"
    DEBUG: bool = False

    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    # lazy cached property без использования functools.cached_property
    @property
    def sqlalchemy_database_uri(self) -> str:
        # кэшируем в приватном атрибуте экземпляра, чтобы вычислить только единожды
        cached: Optional[str] = getattr(self, "_sqlalchemy_database_uri", None)
        if cached is not None:
            return cached

        uri = f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        # сохраняем в экземпляре
        object.__setattr__(self, "_sqlalchemy_database_uri", uri)
        return uri

    class Config:
        env_file = ".env"


# создаём глобальный settings экземпляр
settings = Settings()

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app1.config import settings


# Создание движка
engine = create_async_engine(settings.DATABASE_URL)


# Создание генератора сессий
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Создание базовой модели
class Base(DeclarativeBase):
    pass
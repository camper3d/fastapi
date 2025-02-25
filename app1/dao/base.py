from app1.database import async_session_maker
from sqlalchemy import select, insert

# Базовый класс
class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id) # Запрос в базу данных с фильтрацией
            result = await session.execute(query) # Выполнение запроса
            return result.scalar_one_or_none() # Ответ = один или ничего

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by) # Запрос в базу данных с фильтрацией
            result = await session.execute(query) # Выполнение запроса
            return result.scalar_one_or_none() # Ответ = один или ничего

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)  # Запрос в базу данных
            result = await session.execute(query)  # Выполнение запроса
            return result.mappings().all() # Выводит всё

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data) # Добавлениу данных
            await session.execute(query) # Выполнение запроса
            await session.commit() # коммит
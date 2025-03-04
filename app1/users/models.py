from app1.database import Base
from sqlalchemy import Column, Integer, String

# Создание таблицы пользователей
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

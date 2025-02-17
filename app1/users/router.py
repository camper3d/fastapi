from fastapi import APIRouter, HTTPException
from app1.users.auth import get_password_hash
from app1.users.DAO import UsersDAO

from app1.users.schemas import SchemaUserRegister

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Пользователи'],
)

@router.post('/register')
async def register_user(user_data: SchemaUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email) # Проверка пользователя
    if existing_user:
        raise HTTPException(status_code=400)
    hashed_password = get_password_hash(user_data.password) # Хеширование пароля пользователя
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password) # Заносим в базу данных емаил и хешированный пароль
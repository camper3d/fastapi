from fastapi import APIRouter, HTTPException, status, Response
from app1.users.auth import get_password_hash
from app1.users.DAO import UsersDAO

from app1.users.schemas import SchemaUserAuth
from app1.users.auth import authenticate_user, create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Пользователи'],
)

@router.post('/register')
async def register_user(user_data: SchemaUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email) # Проверка пользователя
    if existing_user:
        raise HTTPException(status_code=500) # Если пользователь есть, возвращаем ошибку
    hashed_password = get_password_hash(user_data.password) # Хеширование пароля пользователя
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password) # Заносим в базу данных емаил и хешированный пароль


@router.post('/login')
async def login_user(response: Response, user_data: SchemaUserAuth):
    user = await authenticate_user(user_data.email, user_data.password) # Проверка маила, юзера, пароля
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) # Ошибка авторизации
    access_token = create_access_token({'sub': user.id}) # Создание токен доступа
    response.ser_cookie('booking_access_token', access_token, httponly=True) # Сэтим куку, httponly=True, чтобы нельзя было достать куку через js
    return {'access_token': access_token}
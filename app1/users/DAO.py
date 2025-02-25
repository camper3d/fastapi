from app1.dao.base import BaseDAO
from app1.users.models import Users

# Базовый класс, модель - пользователь
class UsersDAO(BaseDAO):
    model = Users
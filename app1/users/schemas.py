from pydantic import BaseModel, EmailStr

# Схема для тела запроса
class SchemaUserRegister(BaseModel):
    email: EmailStr
    password: str
from pydantic import BaseModel, EmailStr

# Схема для тела запроса
class SchemaUserAuth(BaseModel):
    email: EmailStr
    password: str
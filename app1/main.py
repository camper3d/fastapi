from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app1.bookings.router import router as router_bookings
from app1.users.router import router as router_users

# Создание приложения
app = FastAPI()


# Добавление эндпоинтов
app.include_router(router_users)
app.include_router(router_bookings)

class SchemaHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get('/hotels')
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
) -> list[SchemaHotel]:
    hotels = [
        {
            "address": "ул.Гагарина, 1, Алтай",
            "name": "Super Hotel",
            "stars": 5,
        },
    ]
    return hotels



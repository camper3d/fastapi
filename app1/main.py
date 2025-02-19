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

class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get('/hotels')
def get_hotels(
        search_args: HotelsSearchArgs = Depends()
):
    return search_args


class SchemaBooking(BaseModel):
    room_id: int
    date_from: date
    date_ti: date


@app.post('/bookings')
def add_booking(booking: SchemaBooking):
    pass
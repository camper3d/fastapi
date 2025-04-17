from datetime import date
from fastapi import APIRouter, Request, Depends
from app1.bookings.DAO import BookingDAO
from app1.bookings.schemas import SchemaBooking
from app1.users.dependencies import get_current_user
from app1.users.models import Users
from app1.exceptions import RoomCannotBeBooked



# Создание роутера
router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SchemaBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked



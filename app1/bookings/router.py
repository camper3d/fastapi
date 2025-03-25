from fastapi import APIRouter, Request
from app1.bookings.DAO import BookingDAO
from app1.bookings.schemas import SchemaBooking



# Создание роутера
router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get("")
async def get_bookings(user):
    return await BookingDAO.find_all()



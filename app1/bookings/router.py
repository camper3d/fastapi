from fastapi import APIRouter
from app1.bookings.DAO import BookingDAO
from app1.bookings.schemas import SchemaBooking



# Создание роутера
router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get("")
async def get_bookings() -> list[SchemaBooking]:
     return await BookingDAO.find_all()



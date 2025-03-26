from fastapi import APIRouter, Request, Depends
from app1.bookings.DAO import BookingDAO
from app1.bookings.schemas import SchemaBooking
from app1.users.dependencies import get_current_user
from app1.users.models import Users



# Создание роутера
router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)



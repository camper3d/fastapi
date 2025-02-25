from app1.bookings.models import Bookings
from app1.dao.base import BaseDAO

# Работа с базой данных
class BookingDAO(BaseDAO):
    model = Bookings




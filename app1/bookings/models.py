from app1.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Computed

# Создание таблицы бронирования
class Bookings(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed('(date_to - date_from) * price', persisted=True))
    total_days = Column(Integer, Computed('date_to - date_from', persisted=True))




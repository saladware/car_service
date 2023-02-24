from sqlalchemy.orm import relationship

from ..database import Base
from .schemas import Gender

from sqlalchemy import Column, Text, Enum, text, String, Date, DateTime, func
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    email = Column(String(320), nullable=False, unique=True)
    birthday = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    cars = relationship('Car', back_populates='owner')

from sqlalchemy import Column, Text, Integer, String, text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from ..database import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    manufacturer_id = Column(ForeignKey('manufacturers.id'))
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    issued = Column(Integer, nullable=False)
    model = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    manufacturer = relationship('Manufacturer', lazy="immediate")
    owner = relationship('User', back_populates='cars', lazy="immediate")


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    name = Column(Text, nullable=False, unique=True)



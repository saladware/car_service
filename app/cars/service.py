from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import Manufacturer, Car
from . import schemas
from ..exceptions import ItemAlredyExists, ItemNotFound


async def get_car(session: AsyncSession, car_id: UUID) -> Car:
    query = select(Car).where(Car.id == car_id).limit(1)
    result = await session.execute(query)
    car = result.scalar_one_or_none()
    if car is None:
        raise ItemNotFound('car with this id is not found')
    return car


async def create_car(session: AsyncSession, data: schemas.CreateCar) -> Car:
    car = Car(**data.dict())
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car


async def update_car(session: AsyncSession, car_id: UUID, data: schemas.UpdateCar) -> Car:
    car = await get_car(session, car_id)
    for key, value in data.dict(exclude_none=True).items():
        setattr(car, key, value)
    await session.commit()
    await session.refresh(car)
    return car


async def delete_car(session: AsyncSession, car_id: UUID):
    car = await get_car(session, car_id)
    await session.delete(car)
    await session.commit()


async def get_manufacturer(session: AsyncSession, manufacturer_id: UUID) -> Manufacturer:
    query = select(Manufacturer).where(Manufacturer.id == manufacturer_id).limit(1)
    result = await session.execute(query)
    manufacturer = result.scalar_one_or_none()
    if manufacturer is None:
        raise ItemNotFound('manufacturer with this id is not found')
    return manufacturer


async def create_manufacturer(session: AsyncSession, data: schemas.CreateManufacturer) -> Manufacturer:
    manufacturer = Manufacturer(**data.dict())
    session.add(manufacturer)
    try:
        await session.commit()
    except IntegrityError:
        raise ItemAlredyExists('manufacturer with this name is already exists')
    await session.refresh(manufacturer)
    return manufacturer


async def update_manufacturer(session: AsyncSession, manufacturer_id: UUID,
                              data: schemas.UpdateManufacturer) -> Manufacturer:
    manufacturer = await get_manufacturer(session, manufacturer_id)
    for key, value in data.dict(exclude_none=True).items():
        setattr(manufacturer, key, value)
    await session.commit()
    await session.refresh(manufacturer)
    return manufacturer


async def delete_manufacturer(session: AsyncSession, manufacturer_id: UUID):
    manufacturer = await get_manufacturer(session, manufacturer_id)
    await session.delete(manufacturer)
    await session.commit()

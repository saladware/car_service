from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas, service
from ..database import get_session

cars = APIRouter(prefix='/cars', tags=['cars'])
manufacturers = APIRouter(prefix='/manufacturers', tags=['manufacturers'])


@cars.get('/{car_id}')
async def get_car_by_id(car_id: UUID, db: AsyncSession = Depends(get_session)) -> schemas.Car:
    return await service.get_car(db, car_id)


@cars.post('/')
async def create_car(data: schemas.CreateCar, db: AsyncSession = Depends(get_session)) -> schemas.Car:
    return await service.create_car(db, data)


@cars.put('/{car_id}')
async def change_car_info(car_id: UUID, data: schemas.UpdateCar,
                          db: AsyncSession = Depends(get_session)) -> schemas.Car:
    return await service.update_car(db, car_id, data)


@cars.delete('/{car_id}')
async def delete_car(car_id: UUID, db: AsyncSession = Depends(get_session)):
    await service.delete_car(db, car_id)
    return {'detail': 'success'}


@manufacturers.get('/{manufacturer_id}')
async def get_manufacturer_by_id(manufacturer_id: UUID,
                                 db: AsyncSession = Depends(get_session)) -> schemas.Manufacturer:
    return await service.get_manufacturer(db, manufacturer_id)


@manufacturers.post('/')
async def create_manufacturer(data: schemas.CreateManufacturer,
                              db: AsyncSession = Depends(get_session)) -> schemas.Manufacturer:
    return await service.create_manufacturer(db, data)


@manufacturers.put('/{manufacturer_id}')
async def change_manufacturer_info(manufacturer_id: UUID, data: schemas.UpdateManufacturer,
                                   db: AsyncSession = Depends(get_session)) -> schemas.Manufacturer:
    return await service.update_manufacturer(db, manufacturer_id, data)


@manufacturers.delete('/{manufacturer_id}')
async def delete_manufacturer(manufacturer_id: UUID, db: AsyncSession = Depends(get_session)):
    await service.delete_manufacturer(db, manufacturer_id)
    return {'detail': 'success'}

from uuid import UUID

from fastapi import APIRouter


cars = APIRouter(prefix='/cars', tags=['cars'])


@cars.get('/{car_id}')
async def get_car_by_id(car_id: UUID):
    ...


from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_session
from . import schemas, service

users = APIRouter(prefix='/users', tags=['users'])


@users.get('/{user_id}')
async def get_user_by_id(user_id: UUID, db: AsyncSession = Depends(get_session)) -> schemas.User:
    return await service.get_user(db, user_id)


@users.post('/')
async def register_new_user(data: schemas.CreateUser, db: AsyncSession = Depends(get_session)) -> schemas.User:
    return await service.create_user(db, data)


@users.put('/{user_id}')
async def change_user_info(user_id: UUID, data: schemas.UpdateUser,
                           db: AsyncSession = Depends(get_session)) -> schemas.User:
    return await service.update_user(db, user_id, data)


@users.delete('/{user_id}')
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_session)):
    await service.delete_user(db, user_id)
    return {'detail': 'success'}

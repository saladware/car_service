from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import User
from . import schemas
from ..exceptions import ItemAlredyExists, ItemNotFound


async def get_user(session: AsyncSession, user_id: UUID) -> User:
    query = select(User).where(User.id == user_id).limit(1)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    if user is None:
        raise ItemNotFound('user with this id is not found')
    return user


async def create_user(session: AsyncSession, data: schemas.CreateUser) -> User:
    user = User(**data.dict())
    session.add(user)
    try:
        await session.commit()
    except IntegrityError:
        raise ItemAlredyExists('user with this email already exists')
    await session.refresh(user)
    return user


async def update_user(session: AsyncSession, user_id: UUID, data: schemas.UpdateUser) -> User:
    user = await get_user(session, user_id)
    for key, value in data.dict(exclude_none=True).items():
        setattr(user, key, value)
    try:
        await session.commit()
    except IntegrityError:
        raise ItemAlredyExists('user with this email already exists')
    await session.refresh(user)
    return user


async def delete_user(session: AsyncSession, user_id: UUID):
    user = await get_user(session, user_id)
    await session.delete(user)
    await session.commit()

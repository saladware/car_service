from uuid import UUID
from datetime import date, datetime

from pydantic import BaseModel, EmailStr
from enum import StrEnum


class Gender(StrEnum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    gender: Gender
    birthday: date


class User(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    gender: Gender
    birthday: date
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    name: str | None
    email: EmailStr | None
    gender: Gender | None
    birthday: date | None

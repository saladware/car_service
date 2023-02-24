from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from ..users.schemas import User


class CreateManufacturer(BaseModel):
    name: str


class UpdateManufacturer(BaseModel):
    name: str | None


class Manufacturer(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True


class CreateCar(BaseModel):
    issued: int
    model: str
    owner_id: UUID
    manufacturer_id: UUID | None


class UpdateCar(BaseModel):
    issued: int | None
    model: str | None
    owner_id: UUID | None
    manufacturer_id: UUID | None


class Car(BaseModel):
    id: UUID
    issued: int
    model: str
    owner: User
    manufacturer: Manufacturer | None
    created_at: datetime

    class Config:
        orm_mode = True


from pydantic import BaseModel

from models import CategoryEnum


class AdvertisementCreate(BaseModel):
    name: str
    description: str
    price: int
    category: CategoryEnum


class AdvertisementResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    category: str
    creator_id: int



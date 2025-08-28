from pydantic import BaseModel, Field

from models import CategoryEnum


class AdvertisementCreate(BaseModel):
    name: str
    description: str
    price: int
    category: CategoryEnum = Field(
        description="Выберите категорию из списка",
        examples=[cat.value for cat in CategoryEnum]
    )


class AdvertisementResponse(BaseModel):
    id: int
    uniq_id: str
    name: str
    description: str
    price: int
    category: str
    creator_id: int



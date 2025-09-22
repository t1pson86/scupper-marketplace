from pydantic import BaseModel, Field

from models import CategoryEnum
from typing import Optional, List
from .reviews import ReviewResponse

class AdvertisementCreate(BaseModel):
    name: str
    description: str
    price: int
    category: CategoryEnum = Field(
        description="Выберите категорию из списка",
        examples=[cat.value for cat in CategoryEnum]
    )


class AdvertisementUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    category: Optional[CategoryEnum] = None


class AdvertisementResponse(BaseModel):
    id: int
    uniq_id: str
    name: str
    description: str
    price: int
    category: str
    creator_id: int


class AdvertisementPaginationResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    category: str
    creator_id: int


class AdvertisementReviewResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    category: str
    creator_id: int
    reviews: List[ReviewResponse]

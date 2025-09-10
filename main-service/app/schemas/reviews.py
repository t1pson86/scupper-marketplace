from pydantic import BaseModel, Field

from typing import Optional


class ReviewCreate(BaseModel):
    stars: int = Field(..., ge=1, le=5, description="Rating from 1 to 5 stars")
    description: Optional[str] = Field(None, max_length=500)
    advertisement_id: int


class ReviewResponse(BaseModel):
    stars: int
    description: Optional[str]
    advertisement_id: int
    
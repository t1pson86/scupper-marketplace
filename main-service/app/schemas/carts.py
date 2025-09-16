from pydantic import BaseModel
from datetime import datetime

class CartsBase(BaseModel):
    user_id: int

class CartsCreate(CartsBase):
    pass

class CartsResponse(BaseModel):
    id: int
    user_id: int
    created_at: datetime
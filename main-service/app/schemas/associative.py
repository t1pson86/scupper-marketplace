from pydantic import BaseModel
from datetime import datetime


class AssociativeBase(BaseModel):
    pass

class AssociativeResponse(BaseModel):
    cart_id: int
    advertisement_id: int
    added_at: datetime
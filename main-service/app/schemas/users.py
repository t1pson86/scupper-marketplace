import re
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    telegram_username: str
    telegram_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
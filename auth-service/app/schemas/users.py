import re
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    telegram_username: str
    telegram_id: int


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=100)

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        
        if not re.search(r'[a-zA-Z]', v):
            raise ValueError('Password must contain at least one letter')
        
        if re.search(r'[<>{}|\\?!-+="]', v):
            raise ValueError('Password contains invalid characters')
            
        return v


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


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    telegram_username: Optional[str] = None
    telegram_id: Optional[int] = None

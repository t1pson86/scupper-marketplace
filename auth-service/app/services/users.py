from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from fastapi import HTTPException, status
from typing import Optional

from schemas import UserCreate, UserResponse
from models import UsersModel
from core import jwt_ver

class UsersService:

    def __init__(
        self, 
        session: AsyncSession
    ):
        self.session = session


    async def add_user(
        self,
        user: UserCreate
    ) -> UserResponse:
        username_result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.username==user.username)
        )

        existing_username = username_result.scalars().first()

        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        email_result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.email==user.email)
        )

        existing_email = email_result.scalars().first()

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        new_user = UsersModel(
            username=user.username,
            email=user.email,
            hashed_password=jwt_ver.get_hash_password(
                password=user.password
            )
        )

        self.session.add(new_user)
        await self.session.commit()

        return new_user
    

    async def get_user_by_email(
        self,
        email: str
    ) -> Optional[UsersModel]:
        
        existing_email = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.email==email)
        )

        result = existing_email.scalars().first()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The user is not registered"
            )
        
        return result
    

    async def get_user_by_id(
        self,
        id: int
    ) -> UsersModel:
        
        existing_user = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.id==id)
        )

        result = existing_user.scalars().first()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The user was not found"
            )
        
        if not result.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Inactive user"
            )
        
        return result
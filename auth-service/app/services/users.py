from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from fastapi import HTTPException, status

from schemas import UserCreate
from models import UsersModel
from core import jwt_ver

class UsersService:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_user(
        self,
        user: UserCreate
    ):
        username_result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.username==user.username)
        )

        existing_username = username_result.scalars().first()

        if existing_username:
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        email_result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.email==user.email)
        )

        existing_email = email_result.scalars().first()

        if existing_email:
            return HTTPException(
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
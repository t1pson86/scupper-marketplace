from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from .base_repository import BaseRepository
from database import get_new_async_session
from schemas import UserCreate, UserResponse, UserUpdate
from services import UsersService
from models import UsersModel

class UserRepository(BaseRepository[UserCreate]):
    
    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        super().__init__(session)
        self.users_service = UsersService(
            session=self.session
        )


    async def create(
        self, 
        user: UserCreate
    ) -> UserResponse:
        
        return await self.users_service.add_user(
            user=user
        )
        
        
    async def read(
        self, 
        id: int
    ) -> UsersModel:
        
        return await self.users_service.get_user_by_id(
            id=id
        )
        

    async def update(
        self, 
        user_id: int,
        updt_user: UserUpdate
    ) -> UsersModel:
        
        return await self.users_service.update_user(
            user_id=user_id,
            updt_user=updt_user
        )
    
    
    async def delete(
        self, 
        user_id: int
    ) -> None:
        
        return await self.users_service.delete_user(
            user_id=user_id
        )
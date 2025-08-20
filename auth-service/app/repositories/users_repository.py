from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .base_repository import BaseRepository
from database import get_new_async_session
from schemas import UserCreate, UserResponse
from services import UsersService

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
    ):
        
        return 'ok'
        

    async def update(
        self, 
        user
    ):
        
        return 'ok'
    
    
    async def delete(
        self, 
        id
    ):
        
        return 'ok'
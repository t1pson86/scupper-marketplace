from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .base_repository import BaseRepository
from database import get_new_async_session
from schemas import AdvertisementCreate, AdvertisementResponse
from services import AdvertisementsService
from models import AdvertisementsModel
from typing import Tuple, List

class AdvertisementRepository(BaseRepository[AdvertisementCreate]):
    
    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        super().__init__(session)
        self.advertisements_service = AdvertisementsService(
            session=self.session
        )


    async def create(
        self, 
        advertisement: AdvertisementCreate,
        user_id: int
    ) -> AdvertisementResponse:
        
        return await self.advertisements_service.add_advertisement(
            advertisement=advertisement,
            user_id=user_id
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
        uniq_id: str
    ):
        
        return await self.advertisements_service.delete_advertisement(
            advertisement_id=uniq_id
        )
    
    async def get_all(
        self,
        skip: int = 0, 
        limit: int = 15
    ) -> Tuple[List[AdvertisementsModel], int]:
        
        return await self.advertisements_service.get_advertisments(
            skip=skip, 
            limit=limit
        )
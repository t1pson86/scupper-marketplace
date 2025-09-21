from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from .base_repository import BaseRepository
from database import get_new_async_session
from services import CartsService
from schemas import CartsResponse, AssociativeResponse, CartItemSimpleResponse


class CartsRepository(BaseRepository[CartsResponse]):
    
    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        super().__init__(session)
        self.carts_service = CartsService(
            session=self.session
        )

    async def create(
        self,
        user_id: int
    ) -> CartsResponse:
        
        return await self.carts_service.create_cart(
            user_id=user_id
        )
    

    async def read(
        self,
        user_id: int
    ) -> List[CartItemSimpleResponse]:
        
        return await self.carts_service.get_cart_by_user_id(
            user_id=user_id
        )
        

    async def update(
        self
    ):
        
        pass
    
    
    async def delete(
        self,
        user_id: int,
        advertisement_id: int
    ) -> dict:
        
        return await self.carts_service.delete_ad_on_cart(
            user_id=user_id,
            advertisement_id=advertisement_id
        )
    

    async def add_to_cart(
        self,
        user_id: int,
        advertisement_id: int
    ) -> AssociativeResponse:
        
        return await self.carts_service.add_to_cart(
            user_id=user_id,
            advertisement_id=advertisement_id
        )
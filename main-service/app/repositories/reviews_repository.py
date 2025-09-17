from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Tuple

from .base_repository import BaseRepository
from database import get_new_async_session
from services import ReviewsService
from schemas import ReviewCreate, ReviewResponse
from models import ReviewsModel


class ReviewsRepository(BaseRepository[ReviewCreate]):
    
    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        super().__init__(session)
        self.advertisements_service = ReviewsService(
            session=self.session
        )


    async def create(
        self,
        review: ReviewCreate,
        user_id: int
    ) -> Tuple[ReviewsModel, int]:
        
        return await self.advertisements_service.add_review(
            review=review,
            user_id=user_id
        )
        
    async def read(
        self, 
        id: int
    ):
        
        return 'ok'
        

    async def update(
        self
    ) -> dict:

        pass
    
    
    async def delete(
        self
    ):
        
        pass
    
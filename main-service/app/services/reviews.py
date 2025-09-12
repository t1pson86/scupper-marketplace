from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status
from typing import Tuple

from schemas import ReviewCreate
from models import AdvertisementsModel, ReviewsModel


class ReviewsService:

    def __init__(
        self, 
        session: AsyncSession
    ):
        self.session = session


    async def add_review(
        self, 
        review: ReviewCreate
    ) -> Tuple[ReviewsModel, int]:
        
        current_advertisement = await self.session.execute(
            select(AdvertisementsModel)
            .where(AdvertisementsModel.id==review.advertisement_id)
        )

        result = current_advertisement.scalars().first()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="An ad with this ID was not found!"
            )
        
        new_review = ReviewsModel(
            **review.dict()
        )

        self.session.add(new_review)
        await self.session.commit()

        return new_review, result.creator_id
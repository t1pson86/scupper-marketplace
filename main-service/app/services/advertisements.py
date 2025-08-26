from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from fastapi import HTTPException, status

from schemas import AdvertisementCreate
from models import AdvertisementsModel


class AdvertisementsService:

    def __init__(
        self, 
        session: AsyncSession
    ):
        self.session = session


    async def add_advertisement(
        self,
        advertisement: AdvertisementCreate,
        user_id: int
    ) -> AdvertisementsModel:
        
        new_advertisement = AdvertisementsModel(
            name=advertisement.name,
            description=advertisement.description,
            price=advertisement.price,
            category=advertisement.category,
            creator_id=user_id
        )

        self.session.add(new_advertisement)
        await self.session.commit()

        return new_advertisement

    
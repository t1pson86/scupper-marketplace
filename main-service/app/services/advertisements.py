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
    

    async def delete_advertisement(
        self,
        advertisement_id: str
    ) -> None:
        
        current_advertisement = await self.session.execute(
            select(AdvertisementsModel)
            .where(AdvertisementsModel.uniq_id==advertisement_id)
        )

        result = current_advertisement.scalars().first()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This advertisement not found"
            )
        
        await self.session.delete(result)
        await self.session.commit()

        return None

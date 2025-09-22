from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from schemas import AdvertisementCreate, AdvertisementUpdate
from models import AdvertisementsModel
from typing import Tuple, List


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
    

    async def get_advertisments(
        self,
        skip: int = 0, 
        limit: int = 15
    ) -> Tuple[List[AdvertisementsModel], int]:
        
        advertisments = await self.session.execute(
            select(AdvertisementsModel)
            .order_by(AdvertisementsModel.created_at.desc())
            .offset(skip)
            .limit(limit)
            )
        
        result = advertisments.scalars().all()

        count_result = await self.session.execute(
            select(func.count(AdvertisementsModel.id))
        )

        total_count = count_result.scalar_one()
        
        return result, total_count
    

    async def get_advertisment(
        self,
        advertisement_id: int
    ) -> AdvertisementsModel:
        
        current_advertisment = await self.session.execute(
            select(AdvertisementsModel)
            .options(selectinload(AdvertisementsModel.reviews))
            .where(AdvertisementsModel.id==advertisement_id)
            )
        
        result = current_advertisment.scalars().first()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This ID is not found"
            )
        
        return result
    

    async def update_advertisment(
        self,
        user_id: int,
        advertisment_id: str,
        update_data: AdvertisementUpdate
    ) -> dict:
        
        current_advertisment = await self.session.execute(
            select(AdvertisementsModel)
            .where(AdvertisementsModel.uniq_id==advertisment_id)
        )

        result = current_advertisment.scalars().first()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The advertisment with this id was not found."
            )
        
        if result.creator_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You are not the creator of this ad."
            )
        
        update_dict = update_data.dict(exclude_unset=True)
        
        updt_advertisment = await self.session.execute(
            update(AdvertisementsModel)
            .where(AdvertisementsModel.uniq_id==advertisment_id)
            .values(update_dict)
        )

        await self.session.commit()

        return {"update": True}

    

    async def delete_advertisement(
        self,
        advertisement_id: str,
        user_id: int
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
        
        if result.creator_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You cannot delete this ad because you are not its creator."
            )
        
        await self.session.delete(result)
        await self.session.commit()

        return None
    

    async def buy_a_advertisement(
        self,
        advertisement_id: str,
        user_id: int
    ) -> int:
        
        current_advertisement = await self.session.execute(
            select(AdvertisementsModel)
            .where(AdvertisementsModel.uniq_id==advertisement_id)
        )

        result = current_advertisement.scalar_one_or_none()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This advertisement not found"
            )

        if result.creator_id == user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You can't buy your product."
            )
        
        creator_id = result.creator_id
        
        await self.session.delete(result)
        await self.session.commit()

        return creator_id
        

    

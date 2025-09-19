from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func
# from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from models import CartsModel, CartsAdvertisementsModel




class CartsService:

    def __init__(
        self, 
        session: AsyncSession
    ):
        self.session = session


    async def get_cart(
        self,
        user_id: int
    ) -> None:
        
        current_cart = await self.session.execute(
            select(CartsModel)
            .where(CartsModel.user_id==user_id)
        )

        result = current_cart.scalar_one_or_none()

        if result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You already have a cart"
            )
        
        return None
        


    async def create_cart(
        self,
        user_id: int
    ) -> CartsModel:
        
        existing_cart  = await self.get_cart(
            user_id=user_id
        )

        new_cart = CartsModel(
            user_id=user_id
        )

        self.session.add(new_cart)
        await self.session.commit()

        return new_cart
    


    async def add_to_cart(
        self,
        user_id: int,
        advertisement_id: int
    ) -> CartsAdvertisementsModel:

        current_cart = await self.session.execute(
            select(CartsModel)
            .where(CartsModel.user_id==user_id)
        )

        result = current_cart.scalar_one_or_none()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="You don't have a cart"
            )
        
        new_entry = CartsAdvertisementsModel(
            cart_id=result.id,
            advertisement_id=advertisement_id
        )

        self.session.add(new_entry)
        await self.session.commit()

        return new_entry
        

    async def delete_ad_on_cart(
        self
    ):
        pass



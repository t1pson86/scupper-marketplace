from fastapi import APIRouter, Depends

from schemas import CartsResponse, UserResponse, AssociativeResponse
from clients import auth_client
from repositories import CartsRepository

router = APIRouter()


@router.post('')
async def create_cart(
    carts_repository: CartsRepository = Depends(),
    user_data: UserResponse = Depends(auth_client.verify_token),
) -> CartsResponse:
    
    return await carts_repository.create(
        user_id=user_data["id"]
    )

@router.post('/{advertisement_id}')
async def create_cart(
    advertisement_id: int,
    carts_repository: CartsRepository = Depends(),
    user_data: UserResponse = Depends(auth_client.verify_token),
) -> AssociativeResponse:
    
    return await carts_repository.add_to_cart(
        user_id=user_data["id"],
        advertisement_id=advertisement_id
    )



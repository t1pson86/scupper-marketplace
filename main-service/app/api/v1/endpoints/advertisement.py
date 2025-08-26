from fastapi import APIRouter, Depends

from clients import auth_client
from schemas import AdvertisementCreate, AdvertisementResponse, UserResponse
from repositories import AdvertisementRepository

router = APIRouter()


@router.post('')
async def create_advertisement(
    advertisement: AdvertisementCreate,
    user_data: UserResponse = Depends(auth_client.verify_token),
    advertisements_repository: AdvertisementRepository = Depends()
) -> AdvertisementResponse:
    
    return await advertisements_repository.create(
        advertisement=advertisement,
        user_id=user_data["id"]
    )



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



@router.get('')
async def get_all_advertisment(
    user_data: UserResponse = Depends(auth_client.verify_token)
):
    pass



@router.post('/del')
async def delete_advertisement(
    advertisement_id: str,
    user_data: UserResponse = Depends(auth_client.verify_token),
    advertisements_repository: AdvertisementRepository = Depends()
) -> dict:
    
    await advertisements_repository.delete(
        uniq_id=advertisement_id
    )

    return {"Delete": True}



import math
from fastapi import APIRouter, Depends, Query

from clients import auth_client
from schemas import AdvertisementCreate, AdvertisementReviewResponse, AdvertisementResponse, UserResponse, PaginatedResponse, AdvertisementPaginationResponse, AdvertisementUpdate
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


@router.get('/{advertisement_id}')
async def get_advertisement(
    advertisement_id: int,
    user_data: UserResponse = Depends(auth_client.verify_token),
    advertisements_repository: AdvertisementRepository = Depends()
) -> AdvertisementReviewResponse:
    
    return await advertisements_repository.read(
        advertisement_id=advertisement_id
    )



@router.get('')
async def get_all_advertisments(
    user_data: UserResponse = Depends(auth_client.verify_token),
    advertisements_repository: AdvertisementRepository = Depends(),
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(15, ge=1, le=100, description="Элементов на странице"),
) -> PaginatedResponse:
    
    skip = (page - 1) * limit
    
    advertisements, total_count = await advertisements_repository.get_all(
        skip=skip, 
        limit=limit
        )
    
    total_pages = math.ceil(total_count / limit) if total_count > 0 else 1

    advertisement_schemas = [
        AdvertisementPaginationResponse(
            id=ad.id,
            name=ad.name,
            description=ad.description,
            price=ad.price,
            category=ad.category,
            creator_id=ad.creator_id
        ) for ad in advertisements
    ]
    
    return PaginatedResponse(
        total_count=total_count,
        total_pages=total_pages,
        current_page=page,
        items_per_page=limit,
        items=advertisement_schemas
    )



@router.put('/update')
async def delete_advertisement(
    advertisment_id: str,
    update_data: AdvertisementUpdate,
    user_data: UserResponse = Depends(auth_client.verify_token),
    advertisements_repository: AdvertisementRepository = Depends()
) -> dict:
    
    return await advertisements_repository.update(
        user_id=user_data["id"],
        advertisment_id=advertisment_id,
        update_data=update_data
    )


@router.delete('/del')
async def delete_advertisement(
    advertisement_id: str,
    user_data: UserResponse = Depends(auth_client.verify_token),
    advertisements_repository: AdvertisementRepository = Depends()
) -> dict:
    
    await advertisements_repository.delete(
        uniq_id=advertisement_id,
        user_id=user_data["id"]
    )

    return {"Delete": True}



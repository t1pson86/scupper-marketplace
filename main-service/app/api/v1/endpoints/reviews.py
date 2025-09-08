from fastapi import APIRouter, Depends

from schemas import ReviewCreate, ReviewResponse, UserResponse
from repositories import ReviewsRepository
from clients import auth_client

router = APIRouter()

@router.post('')
async def add_review(
    review: ReviewCreate,
    user_data: UserResponse = Depends(auth_client.verify_token),
    reviws_repository: ReviewsRepository = Depends()
) -> ReviewResponse:
    
    return await reviws_repository.create(
        review=review
    )
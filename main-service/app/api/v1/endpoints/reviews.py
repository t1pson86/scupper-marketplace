import json
from fastapi import APIRouter, Depends
from faststream.rabbit.fastapi import RabbitRouter

from schemas import ReviewCreate, ReviewResponse, UserResponse
from repositories import ReviewsRepository
from clients import auth_client, users_client

router = APIRouter()

rabbit_router = RabbitRouter()

@rabbit_router.post('')
async def create_review(
    review: ReviewCreate,
    user_data: UserResponse = Depends(auth_client.verify_token),
    reviws_repository: ReviewsRepository = Depends()
) -> ReviewResponse:
    
    review_data, creator_id = await reviws_repository.create(
        review=review,
        user_id=user_data.id ## ....
    )

    creator_data = await users_client.get_user(
        user_id=creator_id
    )

    broker_message = json.dumps(
        {
            "telegram_user_id": creator_data["telegram_id"],
            "telegram_message": f"""
Новый отзыв на товар №{review_data.advertisement_id}

Звезды: {review_data.stars}
Описание: {review_data.description}
"""
        }
    )

    await rabbit_router.broker.publish(
        message=broker_message,
        queue="reviews"
    )

    return review_data


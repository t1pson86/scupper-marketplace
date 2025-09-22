import json
from fastapi import APIRouter, Depends
from faststream.rabbit.fastapi import RabbitRouter

from schemas import UserResponse
from clients import auth_client, users_client
from repositories import AdvertisementRepository


router = APIRouter()

rabbit_router = RabbitRouter()

@rabbit_router.post('/{advertisement_id}')
async def buy_a_ad(
    advertisement_id: str,
    user_data: UserResponse = Depends(auth_client.verify_token),
    advertisements_repository: AdvertisementRepository = Depends()
):
    
    purchase_information = await advertisements_repository.buy_a_advertisement(
        advertisement_id=advertisement_id,
        user_id=user_data["id"]
    )

    creator_data = await users_client.get_user(
        user_id=purchase_information
    )

    broker_message = json.dumps(
        {
            "telegram_user_id": creator_data["telegram_id"],
            "telegram_message": f"""
Подравляем!
У вас приобрели товар!

Пожалуйста отправьте заказ покупателю.
"""
        }
    )

    await rabbit_router.broker.publish(
        message=broker_message,
        queue="purchases"
    )

    return {"buy": True}
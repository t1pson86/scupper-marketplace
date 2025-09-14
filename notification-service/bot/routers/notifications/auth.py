import json
from aiogram import Bot, Router
from faststream.rabbit import RabbitBroker

from core import bot_settings

bot = Bot(token=bot_settings.bot_token)

router = Router()

rabbit_broker = RabbitBroker()

@rabbit_broker.subscriber("users_login")
async def message_auth(
    broker_message
) -> str:
    
    message_data = json.loads(
        broker_message
    )

    try:

        await bot.send_message(
            chat_id=message_data["telegram_user_id"],
            text=message_data["telegram_message"]
        )

    except Exception as e:
        print(e)
import json
from aiogram import Router, Bot
from faststream.rabbit import RabbitBroker


bot = Bot(token="8478036090:AAFIkAtd4COmhGGGYQLkDkwx-EnFGoW8__I")

router = Router()

rabbit_broker = RabbitBroker()

@rabbit_broker.subscriber("advertisements")
async def message_advertisement(
    broker_message
) -> str:
    
    message_data = json.loads(
        broker_message
    )

    try:
        return await bot.send_message(
            chat_id=message_data["telegram_user_id"],
            text=message_data["telegram_message"]
        )
    
    except Exception as e:
        print(e)

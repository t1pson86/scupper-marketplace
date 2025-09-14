import asyncio
from aiogram import Bot, Dispatcher

from routers import router, rabbit_broker

bot = Bot(token="8478036090:AAFIkAtd4COmhGGGYQLkDkwx-EnFGoW8__I")

dp = Dispatcher()
dp.include_router(router=router)



async def main():
    async with rabbit_broker:
        await rabbit_broker.start()
        print('Брокер стратовал')
        await dp.start_polling(bot)
    print('Брокер стопнулся')

if __name__ == "__main__":
    asyncio.run(main())
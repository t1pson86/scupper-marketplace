from aiogram import Router
from faststream.rabbit import RabbitBroker

from .notifications import advertisement, reviews, auth, purchases

router = Router(name="Notification Service")

router.include_router(
    router=advertisement.router
)

router.include_router(
    router=reviews.router
)

router.include_router(
    router=auth.router
)

router.include_router(
    router=purchases.router
)


rabbit_broker = RabbitBroker()

rabbit_broker.include_router(
    router=reviews.rabbit_broker
)

rabbit_broker.include_router(
    router=advertisement.rabbit_broker
)

rabbit_broker.include_router(
    router=auth.rabbit_broker
)

rabbit_broker.include_router(
    router=purchases.rabbit_broker
)




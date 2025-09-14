from aiogram import Router
from faststream.rabbit import RabbitBroker

from .notifications import advertisement, reviews, auth

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




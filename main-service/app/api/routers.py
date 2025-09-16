from fastapi import APIRouter

from .v1.endpoints import advertisement, reviews, carts

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(
    router=advertisement.router,
    tags=["Main Service Advertisements"],
    prefix='/advertisements'
)

router.include_router(
    router=advertisement.rabbit_router,
    tags=["Main Service Advertisements RabbitMQ"],
    prefix='/advertisements'
)

router.include_router(
    router=reviews.router,
    tags=["Main Service Reviews"],
    prefix='/reviews'
)

router.include_router(
    router=reviews.rabbit_router,
    tags=["Main Service Reviews RabbitMQ"],
    prefix='/reviews'
)

router.include_router(
    router=carts.router,
    tags=["Main Service Carts"],
    prefix='/carts'
)
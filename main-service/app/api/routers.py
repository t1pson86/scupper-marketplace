from fastapi import APIRouter

from .v1.endpoints import advertisement, reviews

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(
    router=advertisement.router,
    tags=["Main Service Advertisement"],
    prefix='/advertisements'
)

router.include_router(
    router=reviews.router,
    tags=["Main Service Reviews"],
    prefix='/reviews'
)
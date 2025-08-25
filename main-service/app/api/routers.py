from fastapi import APIRouter

from .v1.endpoints import advertisement

router = APIRouter(
    prefix="/api/v1",
    tags=["Main Service"]
)

router.include_router(
    router=advertisement.router,
    prefix='/all_users'
)
from fastapi import APIRouter

from .v1.endpoints import auth

router = APIRouter(
    prefix="/api/v1",
    tags=["Main Auth"]
)

router.include_router(
    router=auth.router,
    prefix="/auth"
)
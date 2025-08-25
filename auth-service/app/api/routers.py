from fastapi import APIRouter

from .v1.endpoints import auth

auth_router = APIRouter(
    prefix="/api/v1",
    tags=["Auth Service"]
)

auth_router.include_router(
    router=auth.router,
    prefix="/auth"
)
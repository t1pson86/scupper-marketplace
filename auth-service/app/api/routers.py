from fastapi import APIRouter

from .v1.endpoints import auth, users

auth_router = APIRouter(
    prefix="/api/v1"
)

auth_router.include_router(
    router=auth.router,
    prefix="/auth",
    tags=["Auth Service"]
)

auth_router.include_router(
    router=users.router,
    prefix="/users/data",
    tags=["Users Data"]
)
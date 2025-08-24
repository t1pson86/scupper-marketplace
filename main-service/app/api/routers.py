from fastapi import APIRouter

from .v1.endpoints import users

router = APIRouter()

router.include_router(
    router=users.router
)
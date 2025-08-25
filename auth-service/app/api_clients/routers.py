from fastapi import APIRouter

from .v1.endpoints import users

client_router = APIRouter(
    prefix="/api_client/v1",
    tags=["Client Api"]
)

client_router.include_router(
    router=users.router,
    prefix="/users"
)


from fastapi import APIRouter, Depends

from schemas import UserCreate, UserResponse
from repositories import UserRepository

router = APIRouter()

@router.post('/users', response_model=UserResponse)
async def add_user(
    user: UserCreate,
    users_repo: UserRepository = Depends()
) -> UserResponse:
    
    return await users_repo.create(
        user=user
    )
from fastapi import APIRouter, Depends

from schemas import UserResponse
from dependencies import TokenDep
from repositories import UserRepository

router = APIRouter()


@router.get('')
async def user_verification(
    current_user: UserResponse = Depends(TokenDep())
) -> UserResponse:
    
    return current_user


@router.get('/{user_id}')
async def get_user_by_id(
    user_id: int,
    users_repository: UserRepository = Depends()
) -> UserResponse:
    
    return await users_repository.read(
        id=user_id
    )
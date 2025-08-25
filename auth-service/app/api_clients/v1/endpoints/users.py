from fastapi import APIRouter, Depends

from schemas import UserResponse
from dependencies import TokenDep

router = APIRouter()

@router.get('')
async def user_verification(
    current_user: UserResponse = Depends(TokenDep())
) -> UserResponse:
    
    return current_user
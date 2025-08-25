from fastapi import APIRouter, Depends

from clients import auth_client
from schemas import UserResponse

router = APIRouter()


@router.get('')
async def get_all(
    user_data = Depends(auth_client.verify_token)
) -> UserResponse:
    
    return user_data



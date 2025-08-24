from fastapi import APIRouter, Depends

from client import auth_client

router = APIRouter()


@router.get('/users')
async def get_all(
    user = Depends(auth_client.verify_token)
) -> dict:
    return {"message": True}

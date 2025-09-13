from fastapi import APIRouter, Depends, Request, Response

from repositories import UserRepository
from schemas import UserResponse, UserUpdate
from dependencies import get_current_user, delete_current_user


router = APIRouter()


@router.get('/{user_id}')
async def get_user_by_id(
    user_id: int,
    current_user: UserResponse = Depends(get_current_user),
    users_repository: UserRepository = Depends()
) -> UserResponse:
    
    return await users_repository.read(
        id=user_id
    )


@router.put('')
async def update_user_data(
    updt_user: UserUpdate,
    current_user: UserResponse = Depends(get_current_user),
    users_repository: UserRepository = Depends()
) -> UserResponse:
    
    return await users_repository.update(
        user_id=current_user.id,
        updt_user=updt_user
    )


@router.delete('')
async def delete_user(
    request: Request,
    response: Response,
    current_user: UserResponse = Depends(get_current_user),
    users_repository: UserRepository = Depends()
) -> dict:
    
    delete_data = await users_repository.delete(
        user_id=current_user.id
    )

    await delete_current_user(
        request=request,
        response=response
    )

    return {"delete": True}
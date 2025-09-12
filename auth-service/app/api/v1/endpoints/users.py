from fastapi import APIRouter


router = APIRouter(
    
)


@router.get('/{user_id}')
async def get_user_by_id(
    user_id: int
):
    
    return {"message": "True"}
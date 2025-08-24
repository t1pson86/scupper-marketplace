from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas import UserCreate, UserResponse, TokenBase
from repositories import UserRepository
from services import AuthService
from ...dependencies import logout_current_user, TokenDep


router = APIRouter()


@router.post('/register')
async def register(
    user: UserCreate,
    users_repo: UserRepository = Depends()
) -> UserResponse:
    
    return await users_repo.create(
        user=user
    )


@router.post('/login')
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends()
) -> TokenBase:
    
    existing_user = await auth_service.authenticate_user(
        email=form_data.username,
        password=form_data.password
    )

    jwt_data = await auth_service.create_tokens(
        user_id=existing_user.id
    )

    return jwt_data


@router.post("/logout")
async def logout(
    data_tokens: bool = Depends(logout_current_user)
) -> dict:
    
    return {"message": "Logout is True"}


@router.get('')
async def user_verification(
    current_user: TokenDep = Depends(TokenDep)
) -> UserResponse:
    
    return current_user
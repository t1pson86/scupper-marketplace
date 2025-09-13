import json
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from faststream.rabbit.fastapi import RabbitRouter
from datetime import datetime

from schemas import UserCreate, UserResponse, TokenBase
from repositories import UserRepository
from services import AuthService

from dependencies import logout_current_user


router = APIRouter()

rabbit_router = RabbitRouter()


@router.post('/register')
async def register(
    user: UserCreate,
    users_repo: UserRepository = Depends()
) -> UserResponse:
    
    return await users_repo.create(
        user=user
    )


@rabbit_router.post('/login')
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

    broker_message = json.dumps(
        {
            "telegram_user_id": existing_user.telegram_id,
            "telegram_message": f"""
Выполнен вход в аккаунт {existing_user.username}
- Время захода {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}
"""
        }
    )

    await rabbit_router.broker.publish(
        message=broker_message,
        queue="users_login"
    )

    return jwt_data


@router.post("/logout")
async def logout(
    data_tokens: bool = Depends(logout_current_user)
) -> dict:
    
    return {"message": "Logout is True"}



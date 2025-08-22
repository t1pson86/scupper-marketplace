from fastapi import Depends, HTTPException, status, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_new_async_session
from core import jwt_ver
from models import UsersModel
from .users import UsersService
from schemas import TokenBase
from .cookie import CookieService


class AuthService:


    def __init__(
        self, 
        response: Response,
        request: Request,
        session: AsyncSession = Depends(get_new_async_session)
    ):
        self.session = session
        self.users_service = UsersService(
            session=self.session
        )
        self.cookies_service = CookieService(
            request=request,
            response=response
        )



    async def authenticate_user(
        self, 
        email: str, 
        password: str
    ) -> UsersModel:
        
        existing_user = await self.users_service.get_user_by_email(
            email=email
        )

        password_ver = jwt_ver.get_verify_password(
            plain_password=password,
            hashed_password=existing_user.hashed_password
        )
        
        return existing_user
        


    async def create_tokens(
        self,
        user_id: int
    ) -> TokenBase:
                
        access_token = jwt_ver.create_access_token(
            data={"sub": str(user_id)}
        )
        
        refresh_token = jwt_ver.create_refresh_token(
            data={"sub": str(user_id)}
        )

        self.cookies_service.set_access_token_on_cookie(
            access_token=access_token
        )
        self.cookies_service.set_refresh_token_on_cookie(
            refresh_token=refresh_token
        )

        return TokenBase(
            access_token=access_token,
            refresh_token=refresh_token
        )
from fastapi import HTTPException, Depends, status, Request, Response
from fastapi.security import OAuth2
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_new_async_session
from core import jwt_ver
from services import CookieService
from repositories import UserRepository
from schemas import UserResponse


class Oauth2CookieBearer(OAuth2):

    async def __call__(
        self, 
        request: Request, 
        response: Response,
        session: AsyncSession = Depends(get_new_async_session)
    ):
        access_token = request.cookies.get("access_token")
        refresh_token = request.cookies.get("refresh_token")

        if access_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The user is not logged in"
            )
        
        if refresh_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The user is not logged in"
            )
        
        jwt_payload = jwt_ver.decode_token(
            token = access_token
        )

        if jwt_payload.sub is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Could not validate credentials"
            )
        
        users_repo = UserRepository(
            session=session
        )

        current_user = await users_repo.read(
            id = int(jwt_payload.sub)
        )

        new_access_token = jwt_ver.create_access_token(
            data={"sub": str(jwt_payload.sub)}
        )
        
        cookies_service = CookieService(
            request=request,
            response=response
        )

        cookies_service.set_access_token_on_cookie(
            access_token=new_access_token
        )
        
        return current_user

Oauth2Cookie_scheme = Oauth2CookieBearer()



async def get_current_user(
    user: UserResponse = Depends(Oauth2Cookie_scheme)
) -> UserResponse:
    
    return user


async def logout_current_user(
    request: Request,
    response: Response,
    user: UserResponse = Depends(Oauth2Cookie_scheme)
):
    cookies_service = CookieService(
        request=request,
        response=response
    )

    cookies_service.delete_tokens()

    return True
    
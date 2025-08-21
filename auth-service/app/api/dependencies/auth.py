from fastapi import HTTPException, Depends, status, Request, Response
from fastapi.security import OAuth2
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError

from database import get_new_async_session
from core import jwt_ver, jwt_settings
from services import CookieService


class Oauth2CookieBearer(OAuth2):

    def __call__(
        self, 
        request: Request, 
        response: Response
    ):
        access_token = request.cookies.get("access_token")
        refresh_token = request.cookies.get("refresh_token")

        if refresh_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The user is not logged in"
            )
        
        jwt_payload = jwt_ver.decode_token(
            token = refresh_token
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
        
        return new_access_token

Oauth2Cookie_scheme = Oauth2CookieBearer()



async def get_current_user(
    session: AsyncSession = Depends(get_new_async_session),
    token: str = Depends(Oauth2Cookie_scheme)
):
    jwt_payload = jwt_ver.decode_token(
        token
    )
    # if payload.sub is None: разкомитить
    #     raise ...
    
    user_repo = UserRepository(
        session=session
    )
    current_user = await user_repo.read(
        id = int(payload.sub)
    )
    return current_user
    
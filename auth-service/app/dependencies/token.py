from fastapi import HTTPException, status, Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from core import jwt_ver
from repositories import UserRepository
from database import get_new_async_session
from services import CookieService
from schemas import UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenDep:

    async def __call__(
        self,
        request: Request,
        response: Response,
        session: AsyncSession = Depends(get_new_async_session),
        token: str = Depends(oauth2_scheme)
    ) -> UserResponse:

        jwt_payload = jwt_ver.decode_token(
            token = token
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
            id=int(jwt_payload.sub)
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
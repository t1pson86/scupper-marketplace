import aiohttp
from fastapi import HTTPException, status, Request

class UsersClient:
    
    async def verify_token(
        self,
        request: Request
    ):
        cookies_token = request.cookies.get("access_token")

        if cookies_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The user is not logged in"
            )
        
        headers = {"Authorization": f"Bearer {cookies_token}"}
        
        try:
            async with aiohttp.ClientSession() as http_session:
                async with http_session.get(
                    "http://127.0.0.1:8000/api_client/v1/users",
                    headers=headers,
                    timeout=5
                ) as response:
                    
                    if response.status == 200:
                        return await response.json()

                    if response.status == 401:
                        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User not authorized"
                        )

                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="Auth service error"
                    )
                        
        except aiohttp.ClientError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Auth service unavailable"
            )

auth_client = AuthClient()
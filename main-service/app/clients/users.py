import aiohttp
from fastapi import HTTPException, status

from schemas import UserResponse

class UsersClient:
    
    async def get_user(
        self,
        user_id: int
    ) -> UserResponse:
                
        try:
            async with aiohttp.ClientSession() as http_session:
                async with http_session.get(
                    f"http://127.0.0.1:8000/api_client/v1/users/{user_id}",
                    timeout=10
                ) as response:
                    
                    if response.status == 200:
                        return await response.json()
                    
                    if response.status == 404:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="The user was not found"
                        )
        
                    if response.status == 400:
                        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Inactive user"
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

users_client = UsersClient()
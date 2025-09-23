from fastapi import Depends, HTTPException, status

from cache import client
from schemas import UserResponse
from clients import auth_client


class Rate_Limiter():

    def __init__(self, rate_limit: int):
        self.rate_limit = rate_limit

    async def __call__(
        self,
        user_data: UserResponse = Depends(auth_client.verify_token)
    ):
        user_id = user_data["id"]
        key = f"name=users:rate_limiter:{user_id}"

        current_requests = client.incr(
            name=key
        )
        if current_requests == 1:
            client.expire(key, 60)

        if current_requests > self.rate_limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="To many requests, pls wait..."
            )
        
        

        
        

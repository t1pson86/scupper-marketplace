from fastapi import HTTPException, status, Request, Response


class CookieService:

    def __init__(
        self,
        request: Request, 
        response: Response
    ):
        self.request = request
        self.response = response


    def set_access_token_on_cookie(
        self,
        access_token: str
    ) -> bool:
        
        # if self.request.cookies.get("access_token"):
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail='The user is already authenticated'
        #     )
        
        self.response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,     
            secure=True,         
            samesite="lax",
            max_age=1800
        )

        return True
    

    def set_refresh_token_on_cookie(
        self, 
        refresh_token: str
    ) -> bool:
        
        # if self.request.cookies.get("refresh_token"):
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail='The user is already authenticated'
        #     )
        
        self.response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,     
            secure=True,         
            samesite="lax"
        )
        return True
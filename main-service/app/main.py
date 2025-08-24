import uvicorn
from fastapi import FastAPI

from api import router

app = FastAPI()
app.include_router(
    router=router
)


if __name__ == '__main__':
    try:
        uvicorn.run(
            "main:app",
            reload=True,
            port=8001
        )
    except Exception as e:
        print('Error')
        print(e)
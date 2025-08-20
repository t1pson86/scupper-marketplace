import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


# -- DATABASE SETTINGS -- 
class DatabaseSettings(BaseSettings):
    postgres_url: str = f'postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'

db_settings = DatabaseSettings()


# -- JWT SETTINGS --
class JWTSettings(BaseSettings):

    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: int = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
    JWT_TOKEN_TYPE: str = os.getenv("JWT_TOKEN_TYPE")
    
    class Config:
        env_file = ".env"


jwt_settings = JWTSettings()
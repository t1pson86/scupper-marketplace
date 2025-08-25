import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


# -- DATABASE SETTINGS -- 
class DatabaseSettings(BaseSettings):
    postgres_url: str = f'postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'

db_settings = DatabaseSettings()


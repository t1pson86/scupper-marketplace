import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


# -- BOT SETTINGS -- 
class BotSettings(BaseSettings):
    bot_token: str = os.getenv("BOT_TOKEN")

bot_settings = BotSettings()
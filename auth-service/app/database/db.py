from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from core import db_settings

class DatabaseSession:

    def __init__(self):
        self.engin = create_async_engine(
            url = db_settings.postgres_url,
            echo = False
        )
        self.async_session = async_sessionmaker(
            bind = self.engin,
            class_ = AsyncSession,
            expire_on_commit = False
        )

db_session = DatabaseSession()
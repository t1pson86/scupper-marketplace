from .db import db_session


async def get_new_async_session():
    async with db_session.async_session() as session:
        yield session
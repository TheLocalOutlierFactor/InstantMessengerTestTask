from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_HOST, DATABASE_PORT

DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session_maker  = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker () as session:
        yield session

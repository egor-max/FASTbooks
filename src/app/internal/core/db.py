from typing import AsyncGenerator

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import(
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from settings import settings

Asyncengine = create_async_engine(
    settings.database_url, 
    connect_args={
        "check_same_thread": False
        },
    )
AsyncSessionLocal = async_sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=Asyncengine,
    )


Base = declarative_base()

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Запуск асинхронных сессий. 

    Yields
    ------        
        AsyncGenerator[AsyncSessionLocal, None]: _description_

    """

    async with AsyncSessionLocal() as session:
        yield session

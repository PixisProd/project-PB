from typing import Annotated

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from fastapi import Depends

from server.src.config import settings
from server.src.models import OrmBase


DATABASE_URL_PARAMETERS = f'{settings.PG_USER.get_secret_value()}:{settings.PG_PASSWORD.get_secret_value()}@{settings.PG_HOST}/{settings.PG_DATABASE_NAME}'
DATABASE_URL = f'postgresql+asyncpg://{DATABASE_URL_PARAMETERS}'


async_engine = create_async_engine(
    url=DATABASE_URL,
)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

async def get_db():
    async with async_session_factory() as db:
        yield db

db_dependency = Annotated[AsyncSession, Depends(get_db)]

async def create_tables() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(OrmBase.metadata.create_all)

async def drop_tables() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(OrmBase.metadata.drop_all)

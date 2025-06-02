from contextlib import asynccontextmanager

from fastapi import FastAPI

from server.src.database import create_tables, drop_tables
from server.src import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(
    title='PromptBOX API',
    lifespan=lifespan,
)

app.include_router(router)
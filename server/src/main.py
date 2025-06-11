from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from server.src.database import create_tables, drop_tables
from server.src import router, init_handlers
from server.src.logger import setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info('App starting...')
    await create_tables()
    logging.info('App ready')
    yield
    # await drop_tables()
    logging.info('App shutdown')


setup_logger()


app = FastAPI(
    title='PromptBOX API',
    lifespan=lifespan,
)


init_handlers(app)
app.include_router(router)
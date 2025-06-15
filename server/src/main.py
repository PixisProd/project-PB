from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.src.database import create_tables, drop_tables
from server.src import router, init_handlers
from server.src.logger import setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info('App starting...')
    await create_tables()
    logging.info('App ready')
    yield
    await drop_tables()
    logging.info('App shutdown')


setup_logger()


app = FastAPI(
    title='PromptBOX API',
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

init_handlers(app)
app.include_router(router)
from fastapi import APIRouter, FastAPI

from server.src.auth.router import router as auth_router
from server.src.prompts.router import router as prompts_router
from server.src.auth.handlers import init_handlers as auth_handlers
from server.src.prompts.handlers import init_handlers as prompts_handlers


router = APIRouter(
    prefix='/api'
)

v1router = APIRouter(
    prefix='/v1'
)

v1router.include_router(auth_router)
v1router.include_router(prompts_router)


router.include_router(v1router)


def init_handlers(app: FastAPI):
    auth_handlers(app=app)
    prompts_handlers(app=app)
from fastapi import APIRouter

from server.src.auth.router import router as auth_router


router = APIRouter(
    prefix='/api'
)

v1router = APIRouter(
    prefix='/v1'
)

v1router.include_router(auth_router)


router.include_router(v1router)
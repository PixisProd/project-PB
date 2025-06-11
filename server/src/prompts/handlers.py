from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse

from server.src.prompts import exceptions
from server.src.config import settings


def init_handlers(app: FastAPI):
    @app.exception_handler(exceptions.PromptNotFoundException)
    async def prompt_not_found_handler(request: Request, exc: Exception):
        return JSONResponse(
            content={settings.ERROR_MESSAGE_KEY: str(exc)},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    
    @app.exception_handler(exceptions.PromptVarsExceptions)
    async def prompt_vars_handler(request: Request, exc: Exception):
        return JSONResponse(
            content={settings.ERROR_MESSAGE_KEY: str(exc)},
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
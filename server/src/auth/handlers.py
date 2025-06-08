from fastapi import Request, FastAPI, status
from fastapi.responses import JSONResponse

from server.src.auth import exceptions
from server.src.config import settings


def init_handlers(app: FastAPI):
    @app.exception_handler(exceptions.TokenException)
    async def token_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            content={settings.ERROR_MESSAGE_KEY: str(exc)},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    
    @app.exception_handler(exceptions.UserNotFoundException)
    async def user_not_found_handler(request: Request, exc: Exception):
        return JSONResponse(
            content={settings.ERROR_MESSAGE_KEY: str(exc)},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    
    @app.exception_handler(exceptions.DeactivatedUserException)
    async def deactivated_user_handler(request: Request, exc: Exception):
        return JSONResponse(
            content={settings.ERROR_MESSAGE_KEY: str(exc)},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    
    @app.exception_handler(exceptions.IncorrectCredentialsException)
    async def incorrect_credentials_handler(request: Request, exc: Exception):
        return JSONResponse(
            content={settings.ERROR_MESSAGE_KEY: str(exc)},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    
    @app.exception_handler(exceptions.UserAlreadyExistsException)
    async def user_already_exists_handler(request: Request, exc: Exception):
        return JSONResponse(
            content={settings.ERROR_MESSAGE_KEY: str(exc)},
            status_code=status.HTTP_409_CONFLICT,
        )
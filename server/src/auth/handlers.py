from fastapi import Request, FastAPI, HTTPException, status

from server.src.auth import exceptions


def init_handler(app: FastAPI):
    @app.exception_handler(exceptions.TokenException)
    async def token_exception_handler(request: Request, exc: Exception):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        )
    
    @app.exception_handler(exceptions.UserNotFoundException)
    async def user_not_found_exception_handler(
        request: Request,
        exc: Exception,
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )
    
    @app.exception_handler(exceptions.DeactivatedUserException)
    async def deactivated_user_exception(request: Request, exc: Exception):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc)
        )
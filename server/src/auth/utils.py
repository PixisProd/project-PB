from jose import jwt, exceptions
from fastapi import Depends, Cookie, HTTPException, status

from server.src.config import settings
from server.src.security.jwt import decode_token


async def verify_token(
        token: str = Cookie(
            default=None,
            alias=settings.JWT_ACCESS_TOKEN_COOKIE_NAME,
        )
) -> dict:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Missing access token',
        )
    try:
        return await decode_token(token)
    except exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Access token expired',
        )
    except exceptions.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid access token',
        )
import datetime

import jose
from fastapi import Depends, Cookie, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from server.src.config import settings
from server.src.auth import exceptions
from server.src.auth.schemas import AccessTokenPayload
from server.src.auth.service import get_user
from server.src.security.jwt import decode_token, create_access_token


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
    except jose.exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Access token expired',
        )
    except jose.exceptions.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid access token',
        )
    
    
async def refresh_token(
    db: AsyncSession,
    token: str,
):
    try:
        payload = await decode_token(token)
    except jose.exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Refresh token expired',
        )
    except jose.exceptions.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid refresh token',
        )
    try:
        user = await get_user(user_id=int(payload.get('sub')), db=db)
    except exceptions.UserNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User deactivated',
        )
    now = datetime.datetime.now(datetime.UTC)
    new_access_token_payload = AccessTokenPayload(
        email=user.email,
        role=user.role
    )
    new_access_token = await create_access_token(
        user_id=user.id,
        now=now,
        payload=new_access_token_payload.model_dump()
    )
    return new_access_token
    

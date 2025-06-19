import datetime

import jose
from fastapi import Cookie
from sqlalchemy.ext.asyncio import AsyncSession

from server.src.config import settings
from server.src.auth import exceptions
from server.src.auth.schemas import AccessTokenPayload
from server.src.auth.service import get_user
from server.src.security.jwt import decode_token, create_access_token


async def verify_token(
        token: str = Cookie(
            default=None,
            alias=settings.jwt.access_token_cookie_name,
        )
) -> dict:
    if not token:
        raise exceptions.MissingRefreshTokenException()
    try:
        return await decode_token(token)
    except jose.exceptions.ExpiredSignatureError:
        raise exceptions.ExpiredAccessTokenException()
    except jose.exceptions.JWTError:
        raise exceptions.InvalidAccessTokenException()
    
    
async def refresh_token(
    db: AsyncSession,
    token: str,
):
    try:
        payload = await decode_token(token)
    except jose.exceptions.ExpiredSignatureError:
        raise exceptions.ExpiredRefreshTokenException()
    except jose.exceptions.JWTError:
        raise exceptions.InvalidRefreshTokenException()
    user = await get_user(user_id=int(payload.get('sub')), db=db)
    if not user.is_active:
        raise exceptions.DeactivatedUserException()
    now = datetime.datetime.now(datetime.UTC)
    new_access_token_payload = AccessTokenPayload(
        email=user.email,
        role=user.role,
        plan=user.plan,
    )
    new_access_token = await create_access_token(
        user_id=user.id,
        now=now,
        payload=new_access_token_payload.model_dump()
    )
    return new_access_token

import datetime

from jose import jwt

from server.src.config import settings


async def create_token(
    user_id: int,
    now: datetime.datetime,
    lifetime: datetime.timedelta,
    payload: dict = None
) -> str:
    temp_payload = {
        'sub': str(user_id),
        'iat': int(now.timestamp()),
        'exp': int((now + lifetime).timestamp()),
    }
    if payload:
        temp_payload.update(payload)
    return jwt.encode(
        claims=temp_payload,
        key=settings.JWT_SECRET_KEY.get_secret_value(),
        algorithm=settings.JWT_ALGORITHM,
    )

async def create_access_token(
    user_id: int,
    now: datetime.datetime,
    payload: dict,
) -> str:
    return await create_token(
        user_id=user_id,
        now=now,
        lifetime=settings.JWT_ACCESS_TOKEN_LIFETIME,
        payload=payload,
    )

async def create_refresh_token(
    user_id: int,
    now: datetime.datetime,
) -> str:
    return await create_token(
        user_id=user_id,
        now=now,
        lifetime=settings.JWT_REFRESH_TOKEN_LIFETIME,
    )

async def decode_token(token: str) -> dict:
    return jwt.decode(
        token=token,
        key=settings.JWT_SECRET_KEY.get_secret_value(),
        algorithms=settings.JWT_ALGORITHM,
    )
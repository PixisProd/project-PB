import datetime

from fastapi import APIRouter, status, Depends, Cookie
from fastapi.responses import JSONResponse

from server.src.auth.service import register_user, login_user, get_user
from server.src.auth.schemas import (
    RegisterUser, AccessTokenPayload, LoginUser
)
from server.src.auth.utils import refresh_token
from server.src.auth.dependencies import user_dependency
from server.src.auth import exceptions
from server.src.security.jwt import create_access_token, create_refresh_token
from server.src.database import db_dependency
from server.src.config import settings


router = APIRouter(
    prefix='/auth',
    tags=['Auth 🔒'],
)


@router.post('/registration', status_code=status.HTTP_201_CREATED)
async def registration(db: db_dependency, user: RegisterUser) -> None:
    await register_user(user, db)
    return JSONResponse(
        content={'msg': 'User successfully registered'},
        status_code=status.HTTP_201_CREATED,
    )


@router.get('/about')
async def about_user(user: user_dependency, db: db_dependency):
    return await get_user(int(user.get('sub')), db)


@router.post('/login', status_code=status.HTTP_200_OK)
async def login(
    db: db_dependency,
    credentials: LoginUser,
) -> None:
    user = await login_user(credentials, db)
    now = datetime.datetime.now(datetime.UTC)
    access_token_payload = AccessTokenPayload(
        email=user.email,
        role=user.role,
        plan=user.plan,
    )
    access_token = await create_access_token(
        user_id=user.id,
        now=now,
        payload=access_token_payload.model_dump(),
    )
    refresh_token = await create_refresh_token(
        user_id=user.id,
        now=now,   
    )
    response = JSONResponse(
        content={'msg': 'Successful login'},
        status_code=status.HTTP_200_OK,
    )
    response.set_cookie(
        key=settings.jwt.access_token_cookie_name,
        value=access_token,
    )
    response.set_cookie(
        key=settings.jwt.refresh_token_cookie_name,
        value=refresh_token,
    )
    return response


@router.post('/refresh-token')
async def refresh_access_token(
    db: db_dependency,
    token: str = Cookie(
        default=None,
        alias=settings.jwt.refresh_token_cookie_name,
    ),
):
    if not token:
        raise exceptions.MissingRefreshTokenException()
    new_access_token = await refresh_token(db, token)
    response = JSONResponse(
        content={'msg': 'Token successfully refreshed'},
        status_code=status.HTTP_200_OK,
    )
    response.set_cookie(
        key=settings.jwt.access_token_cookie_name,
        value=new_access_token,
    )
    return response
    


@router.get('/is-authorized', status_code=status.HTTP_200_OK)
async def check_auth(_: user_dependency):
    return JSONResponse(
        content={
            'msg': 'You are authorized',
            'auth': True,
        },
        status_code=status.HTTP_200_OK
    )
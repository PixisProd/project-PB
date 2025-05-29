from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from server.src.auth.service import register_user
from server.src.auth.schemas import RegisterUser
from server.src.auth import exceptions
from server.src.database import db_dependency


router = APIRouter(
    prefix='/auth',
    tags=['Auth 🔒'],
)

@router.post('/registration', status_code=status.HTTP_201_CREATED)
async def registration(db: db_dependency, user: RegisterUser):
    try:
        await register_user(
            login=user.login,
            password=user.password,
            username=user.username,
            email=user.email,
            db=db
        )
    except exceptions.UserAlreadyExistsException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )
    return JSONResponse(
        content={'msg': 'User successfully registered'},
        status_code=status.HTTP_201_CREATED,
    )
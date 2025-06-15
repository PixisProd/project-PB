from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from server.src.security.bcrypt import bcrypt_context
from server.src.models import OrmUser
from server.src.auth import exceptions
from server.src.auth.schemas import RegisterUser, LoginUser


async def get_user(user_id: int, db: AsyncSession) -> OrmUser:
    query = select(OrmUser).where(OrmUser.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise exceptions.UserNotFoundException()
    return user


async def register_user(
    user: RegisterUser,
    db: AsyncSession,
) -> None:
    user.password = bcrypt_context.hash(user.password)
    db.add(OrmUser(**user.model_dump()))
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise exceptions.UserAlreadyExistsException()
    

async def login_user(
    credentials: LoginUser,
    db: AsyncSession,
) -> OrmUser:
    query = select(OrmUser).where(OrmUser.email == credentials.email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user or not bcrypt_context.verify(credentials.password, user.password):
        raise exceptions.IncorrectCredentialsException()
    if not user.is_active:
        raise exceptions.DeactivatedUserException()
    return user
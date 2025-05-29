from enum import StrEnum
import datetime

from sqlalchemy import String, Integer, Boolean, Enum, text, DateTime
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class OrmBase(DeclarativeBase):
    pass

class Roles(StrEnum):
    user = 'user'
    moderator = 'moderator'
    admin = 'admin'

class OrmUser(OrmBase):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    login: Mapped[str] = mapped_column(
        String(length=64),
        index=True,
        unique=True,
        nullable=False,
    )
    password: Mapped[str] = mapped_column(String(64), nullable=False)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(
        String(64),
        index=True,
        unique=True,
        nullable=False,
    )
    role: Mapped[Roles] = mapped_column(
        Enum(Roles),
        nullable=False,
        default=Roles.user,
        server_default=text(f"'{Roles.user}'"),
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default=text('true'),
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.UTC),
    )
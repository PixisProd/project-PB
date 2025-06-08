from enum import StrEnum
import datetime

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    Enum,
    text,
    DateTime,
    ForeignKey,
    Text,
    JSON,
    ARRAY,
)
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class OrmBase(DeclarativeBase):
    pass


class OrmPrompt(OrmBase):
    __tablename__ = 'prompts'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(column='users.id', ondelete='CASCADE'),
        index=True,
        nullable=False,
    )
    title: Mapped[str] = mapped_column(
        String(length=64),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    variables: Mapped[dict] = mapped_column(
        JSON,
        nullable=True,
    )
    is_public: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text('false')
    )
    tags: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=True,
    )
    model: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    use_case: Mapped[str] = mapped_column(
        String(100),
        nullable=True,

    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.UTC),
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )


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
        String(64),
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
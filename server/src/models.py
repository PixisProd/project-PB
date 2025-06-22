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


class OrmPromptMixin:
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    variables: Mapped[dict] = mapped_column(JSON, nullable=True)
    tags: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=True)
    model: Mapped[str] = mapped_column(String(64), nullable=False)
    use_case: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.UTC),
    )


class OrmPrompt(OrmBase, OrmPromptMixin):
    __tablename__ = 'prompts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(column='users.id', ondelete='CASCADE'),
        index=True,
        nullable=False,
    )
    is_public: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text('false'),
    )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=text('false'),
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )


class OrmPromptHistory(OrmBase, OrmPromptMixin):
    __tablename__ = 'prompts_versions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    prompt_id: Mapped[int] = mapped_column(
        ForeignKey('prompts.id', ondelete='CASCADE'),
        index=True,
        nullable=False,
    )
    version: Mapped[int] = mapped_column(
        Integer, 
        nullable=False, 
        default=0,
        index=True,
    )


class Roles(StrEnum):
    user = 'user'
    moderator = 'moderator'
    admin = 'admin'

class SubPlans(StrEnum):
    trial = 'trial'
    basic = 'basic'
    standard = 'standard'
    premium = 'premium'

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
        nullable=True,
    )
    password: Mapped[str] = mapped_column(String(64), nullable=False)
    username: Mapped[str] = mapped_column(String(64), nullable=True)
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
    plan: Mapped[SubPlans] = mapped_column(
        Enum(SubPlans),
        nullable=False,
        default=SubPlans.trial,
        server_default=text(f"'{SubPlans.trial}'")
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
import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from server.src.models import (
    OrmPrompt, OrmPromptHistory, OrmPromptMixin, SubPlans
)
from server.src.prompts.schemas import SPrompt, SPromptUpdate
from server.src.prompts import exceptions
from server.src.jinja import parse_vars, render_template
from server.src.subscription_manager import SubscriptionManager


logger = logging.getLogger(__name__)


async def count_prompts(db: AsyncSession, user_id: int):
    stmt = await db.execute(
        select(func.count()).select_from(OrmPrompt)
        .where(
            OrmPrompt.user_id == user_id,
            OrmPrompt.is_deleted == False,
        )
    )
    return stmt.scalar_one_or_none()


async def count_versions(db: AsyncSession, prompt_id: int):
    stmt = await db.execute(
        select(func.count()).select_from(OrmPromptHistory)
        .where(
            OrmPromptHistory.prompt_id == prompt_id,
        )
    )
    return stmt.scalar_one_or_none()


async def delete_prompt_oldest_version(db: AsyncSession, prompt_id: int):
    oldest_ver = (await db.execute(
        select(OrmPromptHistory)
        .where(OrmPromptHistory.prompt_id == prompt_id)
        .order_by(OrmPromptHistory.version.asc())
        .limit(1)
    )).scalar_one_or_none()
    if oldest_ver:
        await db.delete(oldest_ver)
        try:
            await db.commit()
        except Exception:
            logger.error('Error while trying to delete last version of prompt')
            await db.rollback()
            raise

async def render_prompt(
    db: AsyncSession,
    user_id: int,
    prompt_id: int,
    vars: dict,
) -> str:
    prompt = await get_prompt(db, user_id, prompt_id)
    required = set(prompt.variables)
    passed = set(vars.keys())

    missing = required - passed
    extra = passed - required
    if missing:
        raise exceptions.MissingPromptVariablesException(list(missing))
    if extra:
        raise exceptions.ExtraPromptVariablesException(list(extra))
    
    rendered = await render_template(prompt.content, vars)
    return rendered


async def add_prompt(
    sub_manager: SubscriptionManager,
    plan: SubPlans,
    db: AsyncSession,
    user_id: int,
    data: SPrompt,
) -> None:
    user_plan = await sub_manager.get_plan_info(plan)
    user_prompts = await count_prompts(db, user_id)
    if user_prompts >= user_plan.max_prompts:
        raise exceptions.PromptLimitReachedException()
    prompt = OrmPrompt(**data.model_dump())
    prompt.user_id = user_id
    prompt.variables = await parse_vars(prompt.content)
    db.add(prompt)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise


async def get_prompts(
    db: AsyncSession, 
    user_id: int,
    include_deleted: bool = False,
):
    query = select(OrmPrompt).where(OrmPrompt.user_id == user_id)
    if not include_deleted:
        query = query.where(OrmPrompt.is_deleted == False)
    result = await db.execute(query)
    prompts = result.scalars().all()
    return prompts


async def get_prompt(db: AsyncSession, user_id: int, prompt_id: int):
    prompts = await get_prompts(db=db, user_id=user_id)
    for prompt in prompts:
        if prompt.id == prompt_id:
            return prompt
    raise exceptions.PromptNotFoundException()


async def save_prompt(db: AsyncSession, prompt: OrmPrompt):
    fields = OrmPromptMixin.__annotations__.keys()
    base_data = {}
    for field in fields:
        base_data[field] = getattr(prompt, field)
    history = OrmPromptHistory(**base_data)
    history.prompt_id = prompt.id
    result = await db.execute(
        select(OrmPromptHistory)
        .where(OrmPromptHistory.prompt_id == history.prompt_id)
        .order_by(OrmPromptHistory.version.desc())
        .limit(1)
    )
    last_version = result.scalar_one_or_none()
    history.version = (last_version.version + 1) if last_version else 1
    db.add(history)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
    

async def update_prompt(
    sub_manager: SubscriptionManager,
    plan: SubPlans,
    db: AsyncSession, 
    user_id: int, 
    prompt_id: int,
    data: SPromptUpdate,
):
    vals = data.model_dump(exclude_unset=True)
    if not vals:
        raise exceptions.NoParametersException()
    user_plan = await sub_manager.get_plan_info(plan)
    prompt_versions_count = await count_versions(db, prompt_id)
    prompt = await get_prompt(db, user_id, prompt_id)
    if user_plan.max_versions > 0:
        if prompt_versions_count >= user_plan.max_versions:
            await delete_prompt_oldest_version(db, prompt_id)
        await save_prompt(db, prompt)
    for key, value in vals.items():
        setattr(prompt, key, value)

    if 'content' in vals:
        prompt.variables = await parse_vars(prompt.content)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise


async def soft_delete_prompt(db: AsyncSession, user_id: int, prompt_id: int):
    prompt = await get_prompt(db, user_id, prompt_id)
    prompt.is_deleted = True
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
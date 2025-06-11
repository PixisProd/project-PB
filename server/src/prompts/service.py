from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from server.src.models import OrmPrompt
from server.src.prompts.schemas import SPrompt
from server.src.prompts import exceptions
from server.src.jinja import parse_vars, render_template


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
    db: AsyncSession,
    user_id: int,
    data: SPrompt,
) -> None:
    prompt = OrmPrompt(**data.model_dump())
    prompt.user_id = user_id
    prompt.variables = await parse_vars(prompt.content)
    db.add(prompt)
    try:
        await db.commit()
    except Exception as e:
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


async def soft_delete_prompt(db: AsyncSession, user_id: int, prompt_id: int):
    prompt = await get_prompt(db, user_id, prompt_id)
    prompt.is_deleted = True
    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise
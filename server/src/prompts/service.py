from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from server.src.models import OrmPrompt
from server.src.prompts.schemas import SPrompt


async def add_prompt(
    db: AsyncSession,
    user_id: int,
    data: SPrompt,
) -> None:
    prompt = OrmPrompt(**data.model_dump())
    prompt.user_id = user_id
    db.add(prompt)
    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        print(e)


async def get_prompts(
    db: AsyncSession,
    user_id: int,
):
    query = select(OrmPrompt).where(OrmPrompt.user_id == user_id)
    result = await db.execute(query)
    prompts = result.scalars().all()
    return prompts

    
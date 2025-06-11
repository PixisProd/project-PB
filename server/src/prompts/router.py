from fastapi import APIRouter, status, Path
from fastapi.responses import JSONResponse

from server.src.prompts.schemas import SPrompt
from server.src.prompts.service import (
    add_prompt, get_prompts, get_prompt, soft_delete_prompt
)
from server.src.auth.dependencies import user_dependency
from server.src.database import db_dependency


router = APIRouter(
    prefix='/prompts',
    tags=['Prompt 📦']
)


@router.get('/')
async def get_all_prompts(user: user_dependency, db: db_dependency):
    return await get_prompts(db=db, user_id=int(user.get('sub')))


@router.get('/{prompt_id}')
async def get_prompt_by_id(
    user: user_dependency,
    db: db_dependency,
    prompt_id: int = Path(gt=0),
): 
    prompt = await get_prompt(
        db=db,
        user_id=int(user.get('sub')),
        prompt_id=prompt_id,
    )
    return prompt


@router.post('/')
async def create_prompt(
    prompt_data: SPrompt,
    user: user_dependency,
    db: db_dependency,
):
    await add_prompt(
        db=db,
        user_id=int(user.get('sub')),
        data=prompt_data,
    )
    return JSONResponse(
        content={'msg': 'Prompt successfully created!'},
        status_code=status.HTTP_201_CREATED,
    )


@router.delete('/{prompt_id}')
async def delete_prompt(
    user: user_dependency,
    db: db_dependency,
    prompt_id: int = Path(gt=0),
):
    await soft_delete_prompt(db, int(user.get('sub')), prompt_id)
    return JSONResponse(
        content={'msg': 'Prompt successfully deleted'},
        status_code=status.HTTP_200_OK,
    )
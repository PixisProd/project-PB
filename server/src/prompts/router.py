from fastapi import APIRouter, status, Path, Query
from fastapi.responses import JSONResponse

from server.src.prompts.schemas import SPrompt, SPromptRender, SPromptUpdate
from server.src.prompts.service import (
    add_prompt, get_prompts, get_prompt, soft_delete_prompt,
    render_prompt, update_prompt
)
from server.src.auth.dependencies import user_dependency
from server.src.database import db_dependency
from server.src.subscription_manager import sub_manager_depc


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


@router.post('/render')
async def render_prompt_by_id(
    user: user_dependency,
    db: db_dependency,
    data: SPromptRender,
):
    rendered = await render_prompt(
        db=db,
        user_id=int(user.get('sub')),
        prompt_id=data.prompt_id,
        vars=data.vars
    )
    return JSONResponse(
        content={
            'msg': 'Successful render',
            'prompt': rendered
        }
    )


@router.post('/')
async def create_prompt(
    sub_manager: sub_manager_depc,
    prompt_data: SPrompt,
    user: user_dependency,
    db: db_dependency,
):
    await add_prompt(
        sub_manager=sub_manager,
        plan=user.get('plan'),
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


@router.patch('/{prompt_id}')
async def edit_prompt(
    sub_manager: sub_manager_depc,
    user: user_dependency,
    db: db_dependency,
    data: SPromptUpdate,
    prompt_id: int = Path(gt=0),
):
    await update_prompt(sub_manager, user.get('plan'), db, int(user.get('sub')), prompt_id, data)
    return JSONResponse(
        content={'msg': 'Prompt successfully updated'},
        status_code=status.HTTP_200_OK,
    )
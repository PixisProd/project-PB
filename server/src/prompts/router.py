from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from server.src.prompts.schemas import SPrompt
from server.src.prompts.service import add_prompt, get_prompts
from server.src.auth.dependencies import user_dependency
from server.src.database import db_dependency


router = APIRouter(
    prefix='/prompts',
    tags=['Prompt 📦']
)


@router.get('/')
async def get_all_prompts(user: user_dependency, db: db_dependency):
    return await get_prompts(db=db, user_id=int(user.get('sub')))


@router.post('/create')
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
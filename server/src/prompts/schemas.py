from typing import Optional, Dict, List

from pydantic import BaseModel, Field


class SPrompt(BaseModel):
    title: str = Field(min_length=1, max_length=48, examples=['Magic Forest'])
    content: str = Field(min_length=1, examples=['Magic forest, dark fantasy'])
    variables: Optional[Dict[str, str]] = Field(
        default=None,
        examples=[{
            'name': 'name of char in centre',
            'weather': 'weather on picture',
        }],
    )
    is_public: bool = Field(default=False, examples=[False])
    tags: Optional[List[str]] = Field(
        default=None,
        examples=[['dark fantasy', 'forest']],
    )
    model: str = Field(default='Text', examples=['Stable diffusion X'])
    use_case: Optional[str] = Field(
        default=None, 
        min_length=1, 
        max_length=100,
        examples=['Create beautiful picture in dark fantasy'],
    )

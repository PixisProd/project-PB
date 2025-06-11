from typing import Optional, Dict, List

from pydantic import BaseModel, Field


class SPrompt(BaseModel):
    title: str = Field(min_length=1, max_length=48, examples=['Product Desc'])
    content: str = Field(
        min_length=1, 
        examples=[
            ('Write a short description for a product called "(( product_name ))".\n'
            'Target audience: (( target_audience ))\n'
            'Key features: (( features ))\n'
            'Tone of voice: (( tone ))\n'
            'End with a call to action: (( call_to_action ))\n')
        ],
    )
    is_public: bool = Field(default=False, examples=[False])
    tags: Optional[List[str]] = Field(
        default=None,
        examples=[['marketing', 'project']],
    )
    model: str = Field(default='Text', examples=['GPT-4'])
    use_case: Optional[str] = Field(
        default=None, 
        min_length=1, 
        max_length=100,
        examples=['Fast brand descs'],
    )

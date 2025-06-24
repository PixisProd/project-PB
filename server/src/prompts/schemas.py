from typing import Optional, Dict, List, Any

from pydantic import BaseModel, Field


class SPromptUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=48)
    content: Optional[str] = Field(None, min_length=1)
    is_public: bool = None
    tags: Optional[List[str]] = None
    model: Optional[str] = None
    use_case: Optional[str] = Field(None, min_length=1, max_length=100)


class SPromptRender(BaseModel):
    prompt_id: int = Field(gt=0, description='ID of the prompt to render')
    vars: Dict[str, str] = Field(..., description='Template variables for rendering')

    model_config = {
        "json_schema_extra": {
            "example": {
                "prompt_id": 1,
                "vars": {
                    "target_audience": "CEOs",
                    "features": "Lots of cloud space, good prices",
                    "product_name": "PromptBox",
                    "tone": "Productive",
                    "call_to_action": "Let's be a partners",
                },
            }
        }
    }


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

from typing import Optional, Dict, List

from pydantic import BaseModel, Field


class SPrompt(BaseModel):
    title: str = Field(min_length=1, max_length=48)
    content: str = Field(min_length=1)
    variables: Optional[Dict[str, str]] = None
    is_public: bool = Field(default=False)
    tags: Optional[List[str]] = None
    model: str = Field(default='Text')
    use_case: Optional[str] = Field(default=None, min_length=1, max_length=100)

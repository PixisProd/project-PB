from typing import Annotated

from fastapi import Depends

from server.src.auth.utils import verify_token


user_dependency = Annotated[dict, Depends(verify_token)]
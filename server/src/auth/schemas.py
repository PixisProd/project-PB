from pydantic import BaseModel, Field, EmailStr


class RegisterUser(BaseModel):
    password: str = Field(min_length=6, max_length=30, examples=['qwerty123'])
    email: EmailStr = Field(max_length=64, examples=['user@user.com'])


class LoginUser(RegisterUser):
    pass

class AccessTokenPayload(BaseModel):
    email: str
    role: str
    plan: str
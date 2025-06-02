from pydantic import BaseModel, Field, EmailStr


class RegisterUser(BaseModel):
    login: str = Field(min_length=5, max_length=12, examples=['user123'])
    password: str = Field(min_length=6, max_length=30, examples=['qwerty123'])
    username: str = Field(min_length=3, max_length=15, examples=['User'])
    email: EmailStr = Field(max_length=64, examples=['user@user.com'])

class AccessTokenPayload(BaseModel):
    email: str
    role: str
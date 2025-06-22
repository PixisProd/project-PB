from datetime import timedelta

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='DB_')
    host: str
    user: SecretStr
    password: SecretStr
    name: str
    test_name: str

class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='JWT_')
    secret_key: SecretStr
    algorithm: str
    access_token_cookie_name: str
    access_token_lifetime: timedelta = timedelta(minutes=15)
    refresh_token_cookie_name: str
    refresh_token_lifetime: timedelta = timedelta(days=7)

class SubPlanSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='SUB_')
    trial_max_prompts: int
    basic_max_prompts: int
    standard_max_prompts: int
    premium_max_prompts: int
    trial_versions_limit: int
    basic_versions_limit: int
    standard_versions_limit: int
    premium_versions_limit: int
    

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    db: DatabaseSettings = Field(default_factory=DatabaseSettings)
    jwt: JWTSettings = Field(default_factory=JWTSettings)
    sub: SubPlanSettings = Field(default_factory=SubPlanSettings)

    ERROR_MESSAGE_KEY: str

settings = Settings()
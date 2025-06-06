from datetime import timedelta

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PG_HOST: str
    PG_USER: SecretStr
    PG_PASSWORD: SecretStr
    PG_DATABASE_NAME: str
    PG_TEST_DATABASE_NAME: str

    JWT_SECRET_KEY: SecretStr
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_COOKIE_NAME: str
    JWT_ACCESS_TOKEN_LIFETIME: timedelta = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_COOKIE_NAME: str
    JWT_REFRESH_TOKEN_LIFETIME: timedelta = timedelta(days=7)

    ERROR_MESSAGE_KEY: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()
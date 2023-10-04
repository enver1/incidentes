import os
from pydantic_settings import BaseSettings
from functools import lru_cache

# reducir el tiempo de ejecución de la función mediante el uso de la técnica de memorización.
@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"

class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"

class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    API_ENTITY_REPOSITORY: str
    FTP_HOST: str
    FTP_USERNAME: str
    FTP_PASSWORD: str
    DEBUG_MODE: bool
    JWT_ALGORITHM: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str
    EMAIL_USE_TLS: bool
    FRONTEND_HOST: str
    RECLUTAMIENTO_HOST: str


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()

    
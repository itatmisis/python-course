from loguru import logger
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Postgres(BaseModel):
    database: str = "db_main"
    host: str = "localhost"
    port: int = 5432
    username: str = "db_main"
    password: str = "db_main"


class Uvicorn(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class _Settings(BaseSettings):
    pg: Postgres = Postgres()
    uvicorn: Uvicorn = Uvicorn()

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_", env_nested_delimiter="__")


settings = _Settings()
logger.info("settings.inited {}", settings.model_dump_json())

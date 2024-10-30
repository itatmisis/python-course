import multiprocessing as mp

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Postgres(BaseModel):
    database: str = "db_main"
    host: str = "localhost"
    port: int = 5432
    username: str = "db_main"
    password: str = "db_main"


class Uvicorn(BaseModel):
    host: str = "localhost"
    port: int = 8000
    workers: int = mp.cpu_count() * 2 + 1


class _Settings(BaseSettings):
    pg: Postgres = Postgres()
    uvicorn: Uvicorn = Uvicorn()

    model_config = SettingsConfigDict(env_file=".env", env_prefix="app_", env_nested_delimiter="__")


settings = _Settings()

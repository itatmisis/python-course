import multiprocessing as mp

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    server_host: str = "0.0.0.0"  # noqa: S104
    server_port: int = 8000
    server_workers: int = mp.cpu_count()

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
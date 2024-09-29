from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config = Config()

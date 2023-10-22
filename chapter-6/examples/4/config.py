from pydantic_settings import BaseSettings


class Config(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000


config = Config(
    _env_file='.env',
    _env_file_encoding='utf-8',
)

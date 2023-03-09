from pydantic import BaseSettings


class Credentials(BaseSettings):
    telegram_token: str

    class Config:
        env_file = ".env"


credentials = Credentials()

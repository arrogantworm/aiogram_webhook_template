from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    ADMIN_ID: int
    URL_DOMAIN: str
    URL_PATH: str
    SERVER_HOST: str
    SERVER_PORT: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()

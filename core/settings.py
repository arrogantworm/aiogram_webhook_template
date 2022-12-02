from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    ADMIN_ID: SecretStr
    URL_DOMAIN: SecretStr
    URL_PATH: SecretStr
    SERVER_HOST: SecretStr
    SERVER_PORT: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()

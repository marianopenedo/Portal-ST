from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str
    URL_DATABASE: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=['.env.example', '.env'], extra='ignore')

settings = Settings()
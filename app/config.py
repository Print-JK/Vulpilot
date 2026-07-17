from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str = ""

    model: str = "gpt-5.5"

    class Config:
        env_file = ".env"


settings = Settings()
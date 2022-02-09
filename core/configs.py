from pydantic import BaseSettings, Field


class Configurations(BaseSettings):
    API_KEY: str = Field(env='API_KEY')

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Configurations()

from pydantic import BaseSettings, Field


class DatabaseSettings(BaseSettings):

    PORT: str = Field("5432", env="POSTGRES_PORT")
    USER: str = Field("postgres", env="POSTGRES_USER")
    HOST: str = Field("db", env="POSTGRES_HOST")
    PASSWORD: str = Field("postgres", env="POSTGRES_PASSWORD")
    DATABASE: str = Field("postgres", env="POSTGRES_DATABASE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


db_settings = DatabaseSettings()

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from core.config_constants import DEFAULT_DSN, MODELS
from core.database.configs import db_settings

TORTOISE_ORM = {
    "connections": {"default": DEFAULT_DSN.format(
        user=db_settings.USER,
        password=db_settings.PASSWORD,
        host=db_settings.HOST,
        database=db_settings.DATABASE,
        port=db_settings.PORT
    )
    },
    "apps": {
        "models": {
            "models": MODELS,
            "default_connection": "default",
        },
    },
}


def setup_database(app: FastAPI):
    register_tortoise(
        app,
        db_url=DEFAULT_DSN.format(
            user=db_settings.USER,
            password=db_settings.PASSWORD,
            host=db_settings.HOST,
            database=db_settings.DATABASE,
            port=db_settings.PORT
        ),
        modules={"models": MODELS},
        generate_schemas=True,
        add_exception_handlers=True,
    )


Tortoise.init_models(MODELS, 'models')

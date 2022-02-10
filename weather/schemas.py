from datetime import datetime

from pydantic import BaseModel, validator
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator

from weather.models import Weather

WeatherSchema = pydantic_model_creator(Weather)


class WeatherCreateSchema(PydanticModel):
    country_code: str
    city: str
    date: datetime
    response: str


class QueryFields(BaseModel):
    country_code: str
    city: str
    date: datetime

    @validator('country_code')
    def country_code_to_lower(cls, v):
        return v.lower()

    @validator('city')
    def city_to_lower(cls, v):
        return v.lower()

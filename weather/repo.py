from typing import Optional

from weather.models import Weather
from weather.schemas import QueryFields, WeatherCreateSchema, WeatherSchema


class WeatherRepo:

    model = Weather
    schema = WeatherSchema

    async def get_by_fields(self, input_schema: QueryFields) -> Optional[WeatherSchema]:
        if object := await self.model.get_or_none(
                country_code=input_schema.country_code,
                city=input_schema.city,
                date=input_schema.date
        ):
            return await self.schema.from_tortoise_orm(object)
        return None

    async def create(self, input_schema: WeatherCreateSchema) -> WeatherSchema:
        created_object = await self.model.create(**input_schema.dict(exclude_unset=True))
        return await self.schema.from_tortoise_orm(created_object)

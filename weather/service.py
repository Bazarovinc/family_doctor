import json
import time

# import requests
from geopy.geocoders import Nominatim
from httpx import AsyncClient

from core.config_constants import API_URL
from core.configs import config
from core.exceptions.services_exceptions import (BadRequestHTTPException,
                                                 NotAuthenticatedHTTPException)
from weather.repo import WeatherRepo
from weather.schemas import QueryFields, WeatherCreateSchema, WeatherSchema


class WeatherService:

    def __init__(self, repo: WeatherRepo, async_client: AsyncClient):
        self.repo = repo
        self.async_client = async_client

    async def create(self, input_schema: WeatherCreateSchema) -> WeatherSchema:
        return await self.repo.create(input_schema)

    async def get_or_create(self, query_fields: QueryFields) -> dict:
        if weather_data := await self.repo.get_by_fields(query_fields):
            return json.loads(weather_data.response.replace("'", "\""))
        geolocator = Nominatim(user_agent="my_user_agent")
        location = geolocator.geocode(query_fields.country_code + ',' + query_fields.city)
        unix_time = time.mktime(query_fields.date.timetuple())
        response = await self.async_client.get(
            API_URL.format(
                lat=location.latitude,
                lon=location.longitude,
                dt=int(unix_time),
                api_key=config.API_KEY
            )
        )
        if response.status_code == 200:
            response_data = response.json()
            await self.create(
                WeatherCreateSchema(
                    country_code=query_fields.country_code,
                    city=query_fields.city,
                    date=query_fields.date,
                    response=str(response_data)
                )
            )
            return response_data
        elif response.status_code == 401:
            raise NotAuthenticatedHTTPException
        elif response.status_code == 400:
            raise BadRequestHTTPException

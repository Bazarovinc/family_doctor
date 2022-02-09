from datetime import datetime

from fastapi import APIRouter, Depends, Query
from dependency_injector.wiring import Provide, inject
from weather.service import WeatherService
from core.containers.base_container import Container
from weather.schemas import QueryFields
router = APIRouter()


@router.get('')
@inject
async def get_weather(
        query_fields: QueryFields = Depends(),
        service: WeatherService = Depends(Provide[Container.services.weather_service])
):
    return await service.get_or_create(query_fields)

from dependency_injector import containers, providers
from httpx import AsyncClient

from weather.service import WeatherService


class ServicesContainer(containers.DeclarativeContainer):
    repos = providers.DependenciesContainer()
    async_client = providers.Singleton(AsyncClient)
    weather_service = providers.Factory(
        WeatherService,
        repo=repos.weather_repo,
        async_client=async_client
    )

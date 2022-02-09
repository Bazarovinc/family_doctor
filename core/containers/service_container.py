from dependency_injector import containers, providers
from weather.service import WeatherService


class ServicesContainer(containers.DeclarativeContainer):
    repos = providers.DependenciesContainer()
    weather_service = providers.Factory(WeatherService, repo=repos.weather_repo)

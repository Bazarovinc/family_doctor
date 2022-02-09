from dependency_injector import containers, providers
from weather.repo import WeatherRepo


class ReposContainer(containers.DeclarativeContainer):
    weather_repo = providers.Singleton(WeatherRepo)
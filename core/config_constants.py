from typing import List

MODELS: List[str] = [
    'aerich.models',
    'weather.models'
]

WIRING_MODULES: List[str] = [
    'weather.api'
]

DEFAULT_DSN: str = 'postgres://{user}:{password}@{host}:{port}/{database}'
# DEFAULT_DSN = 'postgres://postgres:postgres@localhost:15432'

API_URL: str = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&' \
               'dt={dt}&appid={api_key}'

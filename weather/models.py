from datetime import datetime

from tortoise import fields, models


class Weather(models.Model):
    id: int = fields.IntField(pk=True, description='id')
    date: datetime = fields.DatetimeField(description='Запрашиваемая дата')
    country_code: str = fields.CharField(max_length=5, description='Код страны')
    city: str = fields.CharField(max_length=20, description='Город')
    response: str = fields.TextField(description='Ответ от https://openweathermap.org')

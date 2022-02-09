from core.exceptions.base_http_exception import BaseHTTPException


class NotAuthenticatedHTTPException(BaseHTTPException):
    status = 401
    message = 'Неверный ключ'


class BadRequestHTTPException(BaseHTTPException):
    status = 400
    message = 'Неверно введенные данные'

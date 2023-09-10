
from rest_framework.views import exception_handler
from infrastructure.exceptions.exceptions import BaseCustomException


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None and issubclass(exc, BaseCustomException):
        response.data['errors'] = exc.errors

    return response

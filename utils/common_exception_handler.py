from rest_framework.views import exception_handler
from rest_framework import status
from django.core import exceptions
from http import HTTPStatus
from typing import Any

from rest_framework.views import Response


def api_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    """Custom API exception handler."""

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # if isinstance(exc, exceptions.ValidationError):
    #     data = exc.message_dict
    #     return Response(data=data, status=status.HTTP_400_BAD_REQUEST, )

    if response is not None:
        # Using the description's of the HTTPStatus class as error message.
        http_code_to_message = {v.value: v.description for v in HTTPStatus}

        error_payload = {
            'success': False,
            "status_code": 0,
            "message": "",
            "data": [],
        }

        status_code = response.status_code

        error_payload["status_code"] = status_code
        error_payload["message"] = http_code_to_message[status_code]
        error_payload["data"] = response.data
        response.data = error_payload
    return response

from rest_framework.response import Response
from http import HTTPStatus


class ErrorResponse(Response):
    def __init__(self, *args, **kwargs):
        super(ErrorResponse, self).__init__(*args, **kwargs)
        status_code = 404

        if len(args) > 1:
            status_code = args[1]

        http_code_to_message = {v.value: v.description for v in HTTPStatus}

        error_payload = {
            'success': False,
            "status_code": status_code,
            "message": "",
            "details": [],
        }

        error_payload["message"] = http_code_to_message[status_code]
        error_payload['details'] = args[0]

        self.status_code = status_code
        self.data = error_payload


class SuccessResponse(Response):
    def __init__(self, *args, **kwargs):
        super(SuccessResponse, self).__init__(*args, **kwargs)
        status_code = 200

        if len(args) > 1:
            status_code = args[1]

        http_code_to_message = {v.value: v.description for v in HTTPStatus}

        success_payload = {
            'success': True,
            "status_code": status_code,
            "message": "Data Successfully Fetched!",
            "data": [],
        }

        success_payload["message"] = http_code_to_message[status_code]
        success_payload['data'] = args[0]

        self.status_code = status_code
        self.data = success_payload

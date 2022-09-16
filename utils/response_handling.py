from rest_framework.response import Response


class ErrorResponse(Response):
    def __init__(self, *args, **kwargs):
        super(ErrorResponse, self).__init__(*args, **kwargs)
        self.status_code = 404
        self.data = {
            'success': False,
            'message': args[0]
        }


class SuccessResponse(Response):
    def __init__(self, *args, **kwargs):
        super(SuccessResponse, self).__init__(*args, **kwargs)
        self.status_code = 201

        self.data = {
            'success': True,
            'data': args[0]
        }

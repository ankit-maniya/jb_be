from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.response import Response

from utils.response_handling import ErrorResponse, SuccessResponse

from .user_serializer import UserSerializer

from .user_model import Users
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception as e:
            return ErrorResponse(str(e))
        else:
            # any additional logic
            serializer = self.get_serializer(instance)
            return SuccessResponse(serializer.data)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
        except Exception as e:
            return ErrorResponse(str(e))
        else:
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return SuccessResponse(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        except Exception as e:
            return ErrorResponse(str(e))
        else:
            return SuccessResponse(serializer.data)

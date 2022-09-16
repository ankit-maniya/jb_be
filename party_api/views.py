from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from utils.response_handling import ErrorResponse, SuccessResponse
from .models import Partys

from .serializers import PartyModelSerializer

# Create your views here.


class PartyModelViewSet(viewsets.ModelViewSet):
    serializer_class = PartyModelSerializer
    queryset = Partys.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            is_admin = self.request.user.is_admin
            if is_admin:
                return self.queryset
            return self.queryset.filter(userid=self.request.user)
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={
                                         'user': self.request.user})
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        except Exception as e:
            return ErrorResponse(str(e))
        else:
            return SuccessResponse(serializer.data)

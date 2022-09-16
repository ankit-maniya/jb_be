from json import dump
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Cuttingtypes

from .serializers import CuttingTypesSerializer

from utils.response_handling import SuccessResponse
# Create your views here.


class CuttingTypeModelViewSet(viewsets.ModelViewSet):
    serializer_class = CuttingTypesSerializer
    queryset = Cuttingtypes.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            is_admin = self.request.user.is_admin
            if is_admin:
                return self.queryset
            return self.queryset.filter(userid=self.request.user)
        return []

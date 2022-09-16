from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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

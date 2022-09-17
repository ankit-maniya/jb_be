from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Partys

from .serializers import PartyModelSerializer

from .pagination import StandardResultsSetPagination

from .filters import PartyFilter

from utils.response_handling import SuccessResponse

# Create your views here.


class PartyModelViewSet(viewsets.ModelViewSet):
    serializer_class = PartyModelSerializer
    queryset = Partys.objects.all()
    permission_classes = [IsAuthenticated]

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PartyFilter

    search_fields = ['p_name', 'p_billingname',
                     'p_mobile', 'p_email', 'p_openingbalance']

    ordering_fields = '__all__'
    ordering = ['p_name']

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
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return SuccessResponse(serializer.data, 201)

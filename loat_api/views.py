from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from .filters import LoatFilter

from .pagination import StandardResultsSetPagination

from .models import Loats

from .serializers import LoatsSerializer

from utils.response_handling import ErrorResponse, SuccessResponse
# Create your views here.


class LoatModelViewSet(viewsets.ModelViewSet):
    serializer_class = LoatsSerializer
    queryset = Loats.objects.all()

    permission_classes = [IsAuthenticated]

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LoatFilter

    search_fields = ['l_cuttingtype', 'l_price',
                     'l_numofdimonds', 'partyid__p_name']

    ordering_fields = '__all__'
    ordering = ['l_entrydate']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            is_admin = self.request.user.is_admin
            if is_admin:
                return self.queryset
            return self.queryset.filter(userid=self.request.user)
        return []

    def create(self, request, *args, **kwargs):
        partyId = request.data.get('partyid')
        if partyId is None:
            return ErrorResponse('partyid is required!', 417)

        serializer = self.get_serializer(
            data=request.data, context={'user': self.request.user, 'partyId': partyId})
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return SuccessResponse(serializer.data, 201)

    def update(self, request, *args, **kwargs):
        partial = False

        if request.method == 'PATCH':
            partial = True

        partyId = request.data.get('partyid')
        if partyId is None:
            partyId = 0

        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial, context={'user': self.request.user, 'partyId': partyId})
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return SuccessResponse(serializer.data, 206)

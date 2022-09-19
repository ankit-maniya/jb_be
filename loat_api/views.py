from utils.response_handling import ErrorResponse, SuccessResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from math import ceil
from django.db.models import Sum, Count, Case, When, Value, F, FloatField
from django.db.models.expressions import ExpressionWrapper
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay

from django_filters.rest_framework import DjangoFilterBackend

from .filters import LoatFilter

from .pagination import StandardResultsSetPagination

from .models import Loats

from .serializers import LoatsSerializer

from utils.helpers import uniqueArrOfObjList, filterAmountWithArray

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

    @action(detail=False, methods=['GET'], name='Get Pricing Loat wise with filter of Month, Year, Day')
    def daywise_loats_price_details(self, request, *args, **kwargs):
        user = self.request.user
        f_order = request.query_params.get('order')
        f_year = request.query_params.get('year')

        order = ['-year', 'month', 'day']
        filter = {
            "isactive": True,
            "isdelete": False,
            "userid": user.id,
            "l_entrydate__isnull": False
        }

        if f_year:
            filter['year'] = f_year

        if f_order:
            order = f_order.split(",")

        try:
            db_loats = (Loats.objects.values(
                'l_entrydate',
                year=ExtractYear('l_entrydate'),
                month=ExtractMonth('l_entrydate'),
                day=ExtractDay('l_entrydate')
            ).filter(
                **filter
            ).annotate(
                totalDateWiseLoats=Count('id'),
                totalDimonds=Sum('l_numofdimonds'),
                totalWeight=Sum('l_weight'),
                totalAmounts=ExpressionWrapper(
                    Sum(
                        Case(
                            When(l_multiwithdiamonds=True, then=F(
                                'l_price')*F('l_numofdimonds')),
                            When(l_multiwithdiamonds=False, then=F(
                                'l_price')*F('l_weight')),
                            # default=F('l_price')*F('l_weight'),
                            default=Value(0.0),
                            output_field=FloatField()
                        ),
                    ), output_field=FloatField()
                )
            ).order_by(*order))

            yearWiseLoats = []
            totalYears = uniqueArrOfObjList(db_loats, 'year')

            for year in totalYears:
                loatsObj = filterAmountWithArray(
                    db_loats, 'year', year)

                yearWiseLoats.append({"year": year, **loatsObj})

            return SuccessResponse(yearWiseLoats, 200)
        except Exception as e:
            return ErrorResponse({"db_error": str(e)}, 404)

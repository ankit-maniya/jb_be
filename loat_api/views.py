from utils.response_handling import ErrorResponse, SuccessResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from django.db.models import Sum, Count, Case, When, Value, F, FloatField, IntegerField
from django.db.models.expressions import ExpressionWrapper
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay

from django_filters.rest_framework import DjangoFilterBackend

from .filters import LoatFilter

from .pagination import StandardResultsSetPagination

from .models import Loats

from .serializers import LoatsSerializer

from utils.helpers import uniqueArrOfObjList, filterAmountWithArray, filterDataWithCuttingTypeArray

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
            db_loats = (
                Loats.objects.values(
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
                ).order_by(*order)
            )

            yearWiseLoats = []
            totalYears = uniqueArrOfObjList(db_loats, 'year')

            for year in totalYears:
                loatsObj = filterAmountWithArray(
                    db_loats, 'year', year)

                yearWiseLoats.append({"year": year, **loatsObj})

            return SuccessResponse(yearWiseLoats, 200)
        except Exception as e:
            return ErrorResponse({"db_error": str(e)}, 404)

    @action(detail=False, methods=['GET'], name='Get Pricing Cutting type data with Loat wise filter of Month, Year, Day')
    def partywise_yearwise_loat_totals(self, request, *args, **kwargs):
        #  Year, Month, day Wise all total with cutting type data
        user = self.request.user
        f_order = request.query_params.get('order')
        f_month = request.query_params.get('month')
        f_year = request.query_params.get('year')
        f_partyid = request.query_params.get('partyid')

        if f_partyid is None:
            return ErrorResponse({"fieldError": 'PartyId is Required'}, 404)

        order = ['p_name', 'l_year', 'l_month']
        filter = {
            "isactive": True,
            "isdelete": False,
            "userid": user.id,
            "l_entrydate__isnull": False
        }

        if f_year:
            filter['l_year'] = f_year

        if f_month:
            filter['l_month'] = f_month

        if f_partyid:
            filter['partyid'] = f_partyid

        if f_order:
            order = f_order.split(",")

        try:
            db_Response = (
                Loats.objects.select_related('partyid')
                .values(
                    "partyid",
                    "l_price",
                    "l_year",
                    "l_month",
                    "l_cuttingtype"
                )
                .filter(
                    **filter
                ).annotate(
                    p_name=F("partyid__p_name"),
                    TotalAmounts=ExpressionWrapper(
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
                    ),
                    TotalWeight=ExpressionWrapper(Sum(
                        F("l_weight")
                    ), output_field=FloatField()),
                    TotalDimonds=ExpressionWrapper(Sum(
                        F("l_numofdimonds")
                    ), output_field=IntegerField()),

                    DimondWiseTotalAmount=ExpressionWrapper(
                        Sum(
                            Case(
                                When(l_multiwithdiamonds=True, then=F(
                                    'l_price')*F('l_numofdimonds')),
                                default=Value(0.0),
                                output_field=FloatField()
                            ),
                        ), output_field=FloatField()
                    ),
                    DimondWiseTotalWeight=ExpressionWrapper(
                        Sum(
                            Case(
                                When(l_multiwithdiamonds=True,
                                     then=F("l_weight")),
                                default=Value(0.0),
                                output_field=FloatField()
                            ),
                        ), output_field=FloatField()
                    ),
                    DimondWiseTotalDimonds=ExpressionWrapper(
                        Sum(
                            Case(
                                When(l_multiwithdiamonds=True,
                                     then=F("l_numofdimonds")),
                                default=Value(0),
                                output_field=IntegerField()
                            ),
                        ), output_field=IntegerField()
                    ),
                    WeightWiseTotalAmount=ExpressionWrapper(
                        Sum(
                            Case(
                                When(l_multiwithdiamonds=False, then=F(
                                    'l_price')*F('l_weight')),
                                default=Value(0.0),
                                output_field=FloatField()
                            ),
                        ), output_field=FloatField()
                    ),
                    WeightWiseTotalWeight=ExpressionWrapper(
                        Sum(
                            Case(
                                When(l_multiwithdiamonds=False,
                                     then=F('l_weight')),
                                default=Value(0.0),
                                output_field=FloatField()
                            ),
                        ), output_field=FloatField()
                    ),
                    WeightWiseTotalDimonds=ExpressionWrapper(
                        Sum(
                            Case(
                                When(l_multiwithdiamonds=False, then=F(
                                    'l_numofdimonds')),
                                default=Value(0),
                                output_field=IntegerField()
                            ),
                        ), output_field=IntegerField()
                    ),
                ).order_by(*order)
            )

            iRes = []
            totalYears = uniqueArrOfObjList(db_Response, 'l_year')
            for year in totalYears:
                year_wise_filter = filterDataWithCuttingTypeArray(
                    db_Response, 'l_year', year)

                iRes.append({"l_year": year, **year_wise_filter})

            return SuccessResponse(iRes, 200)
        except Exception as e:
            return ErrorResponse({"db_error": str(e)}, 404)

from django_filters.rest_framework import filters

from django_filters import FilterSet

from .models import Partys


class PartyFilter(FilterSet):
    p_openingbalance = filters.NumberFilter()
    id = filters.NumberFilter()
    isactive = filters.BooleanFilter()
    isdelete = filters.BooleanFilter()
    createdat = filters.DateFilter()
    createdat__gte = filters.DateFilter(
        field_name="createdat", lookup_expr='gte')
    createdat__lte = filters.DateFilter(
        field_name="createdat", lookup_expr='lte')

    class Meta:
        model = Partys
        fields = ['p_name', 'p_billingname', 'p_mobile', 'p_address', 'p_email',
                  'p_openingbalance', 'isactive', 'isdelete', 'createdat', 'updatedat', 'userid', 'id']

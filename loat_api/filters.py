from django_filters.rest_framework import filters

from django_filters import FilterSet

from .models import Loats


class LoatFilter(FilterSet):
    l_weight = filters.NumberFilter()
    l_price = filters.NumberFilter()
    l_month = filters.NumberFilter()
    partyid = filters.NumberFilter()
    l_multiwithdiamonds = filters.BooleanFilter()
    isactive = filters.BooleanFilter()
    isdelete = filters.BooleanFilter()
    l_numofdimonds = filters.NumberFilter()
    l_year = filters.NumberFilter()
    l_weight__gte = filters.NumberFilter(
        field_name="l_weight", lookup_expr='gte')
    l_weight__lte = filters.NumberFilter(
        field_name="l_weight", lookup_expr='lte')
    l_entrydate = filters.DateFilter()
    l_entrydate__gte = filters.DateFilter(
        field_name="l_entrydate", lookup_expr='gte')
    l_entrydate__lte = filters.DateFilter(
        field_name="l_entrydate", lookup_expr='lte')

    class Meta:
        model = Loats
        fields = ['l_numofdimonds', 'isactive', 'l_weight', 'l_price', 'l_month',
                  'l_year', 'l_multiwithdiamonds', 'isdelete', 'partyid', 'l_entrydate']

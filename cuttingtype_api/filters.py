from django_filters.rest_framework import filters

from django_filters import FilterSet

from .models import Cuttingtypes


class CuttingTypeFilter(FilterSet):
    c_id = filters.NumberFilter()
    c_multiwithdiamonds = filters.BooleanFilter()
    isactive = filters.BooleanFilter()
    isdelete = filters.BooleanFilter()
    partyid = filters.NumberFilter()
    c_price = filters.NumberFilter()
    c_colorcode = filters.CharFilter()
    c_price__gte = filters.NumberFilter(
        field_name="l_weight", lookup_expr='gte')
    c_price__lte = filters.NumberFilter(
        field_name="l_weight", lookup_expr='lte')
    createdat = filters.DateFilter()
    createdat__gte = filters.DateFilter(
        field_name="createdat", lookup_expr='gte')
    createdat__lte = filters.DateFilter(
        field_name="createdat", lookup_expr='lte')

    class Meta:
        model = Cuttingtypes
        fields = ['c_id',  'c_multiwithdiamonds', 'c_price', 'c_colorcode',
                  'c_name', 'isdelete', 'isactive', 'partyid__id', 'createdat']

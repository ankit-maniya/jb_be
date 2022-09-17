from rest_framework.pagination import LimitOffsetPagination


class StandardResultsSetPagination(LimitOffsetPagination):
    page_size_query_param = 'page_size'
    default_limit = 100

from rest_framework.pagination import LimitOffsetPagination


class PaginationClass(LimitOffsetPagination):
    max_limit = 3

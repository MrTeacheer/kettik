from rest_framework.pagination import LimitOffsetPagination


class ReviewsPagination(LimitOffsetPagination):
    default_limit = 12


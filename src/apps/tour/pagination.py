from rest_framework.pagination import LimitOffsetPagination


class TourPagination(LimitOffsetPagination):
    default_limit = 12

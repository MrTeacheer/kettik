from . import serializers, services, swagger
from common.base.generics import CustomRetieveAPIView, CustomListAPIView


@swagger.banner_schema
class BannerView(CustomRetieveAPIView):
    serializer_class = serializers.BannerSerializer
    service_class = services.BannerService


@swagger.history_schema
class HistoryView(CustomRetieveAPIView):
    serializer_class = serializers.HistorySerializer
    service_class = services.HistoryService


@swagger.images_schema
class ImagesView(CustomListAPIView):
    serializer_class = serializers.ImagesSerializer
    service_class = services.ImagesService


@swagger.in_digits_schema
class InDigitsView(CustomRetieveAPIView):
    serializer_class = serializers.InDigitsSerializer
    service_class = services.InDigitsService


@swagger.team_schema
class TeamView(CustomListAPIView):
    serializer_class = serializers.TeamSerializer
    service_class = services.TeamService

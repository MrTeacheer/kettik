from . import serializers, services, swagger
from common.base.generics import CustomRetieveAPIView, CustomListAPIView


@swagger.banner_schema
class BannerView(CustomRetieveAPIView):
    serializer_class = serializers.BannerSerializer
    service_class = services.BannerService


@swagger.place_schema
class PlaceView(CustomListAPIView):
    serializer_class = serializers.PlaceSerializer
    service_class = services.PlaceService
    prefetch_ = [
        "images",
    ]

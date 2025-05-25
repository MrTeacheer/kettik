from . import serializers, services, swagger, pagination
from common.base.generics import CustomRetieveAPIView, CustomListAPIView


@swagger.banner_schema
class BannerView(CustomRetieveAPIView):
    serializer_class = serializers.BannerSerializer
    service_class = services.BannerService


@swagger.tour_schema
class TourView(CustomListAPIView):
    serializer_class = serializers.TourSerializer
    service_class = services.TourService
    pagination_class = pagination.TourPagination

    def get_queryset(self, excludes=..., *args, **filters):
        min = self.request.query_params.get("min_days")
        max = self.request.query_params.get("max_days")
        return self.service_class.get_filtered_tours(max_days=max, min_days=min)


@swagger.tour_detail_schema
class TourDetailView(CustomRetieveAPIView):
    serializer_class = serializers.TourDetailSerializer
    service_class = services.TourService
    prefetch_ = ["images", "programs", "disadvantages", "advantages"]
    select_ = ["type", "place"]


@swagger.faq_schema
class FAQView(CustomListAPIView):
    serializer_class = serializers.FAQSerializer
    service_class = services.FAQService

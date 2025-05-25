from . import serializers, services, swagger,pagination
from common.base.generics import CustomRetieveAPIView, CustomListAPIView


@swagger.banner_schema
class BannerView(CustomRetieveAPIView):
    serializer_class = serializers.BannerSerializer
    service_class = services.BannerService


@swagger.article_schema
class ArticleView(CustomListAPIView):
    serializer_class = serializers.ArticleSerializer
    service_class = services.ArticleService
    pagination_class = pagination.ArticlePagination

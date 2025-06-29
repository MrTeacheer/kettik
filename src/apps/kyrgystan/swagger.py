from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from . import serializers

tag = "Kyrgyzstan"

banner_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.BannerSerializer,
    )
)

article_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.ArticleSerializer,
        parameters=[
            OpenApiParameter(
                name="limit",
                location=OpenApiParameter.QUERY,
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name="offset",
                location=OpenApiParameter.QUERY,
                required=False,
                type=int,
            ),
        ],
    )
)
region_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.RegionSerializer,
    )
)
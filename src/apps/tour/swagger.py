from . import serializers
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

tag = "Tour"

banner_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.BannerSerializer,
    )
)

tour_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.TourSerializer,
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
            OpenApiParameter(
                name="max_days",
                location=OpenApiParameter.QUERY,
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name="min_days",
                location=OpenApiParameter.QUERY,
                required=False,
                type=int,
            ),
        ],
    )
)

tour_detail_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.TourDetailSerializer,
    )
)
faq_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.FAQSerializer,
    )
)

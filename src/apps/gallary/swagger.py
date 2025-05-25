from drf_spectacular.utils import extend_schema, extend_schema_view
from . import serializers

tag = "Gallary"

banner_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.BannerSerializer,
    )
)

place_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.PlaceSerializer,
    )
)

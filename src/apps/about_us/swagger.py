from drf_spectacular.utils import extend_schema, extend_schema_view
from . import serializers

tag = "About-Us"

banner_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.BannerSerializer,
    )
)
history_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.HistorySerializer,
    )
)
images_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.ImagesSerializer,
    )
)
in_digits_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.InDigitsSerializer,
    )
)
team_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.TeamSerializer,
    )
)
from drf_spectacular.utils import extend_schema, extend_schema_view
from . import serializers

tag = "MainPage"

banner_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.BannerSerializer,
    )
)

application_schema = extend_schema_view(
    post=extend_schema(
        tags=[tag],
        request=serializers.ApplicationCreateSerializer,
        responses=serializers.ApplicationSerializer,
    )
)
contact_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.ContactsSerializer,
    )
)
reviews_schema = extend_schema_view(
    get=extend_schema(
        tags=[tag],
        responses=serializers.GoogleReviewsSerializer,
    )
)


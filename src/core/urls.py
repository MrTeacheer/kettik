from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("api/summernote/", include("django_summernote.urls")),
    # API
    path("api/v1/main/page/", include("apps.main_page.urls")),
    path("api/v1/gallary/", include("apps.gallary.urls")),
    path("api/v1/about/us/", include("apps.about_us.urls")),
    path("api/v1/kyrgyzstan/", include("apps.kyrgystan.urls")),
    path("api/v1/tours/", include("apps.tour.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

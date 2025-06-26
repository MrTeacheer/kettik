from django.contrib import admin
from . import models
from common.base.trans_checkbox import TranslatorMediaMixin


@admin.register(models.Banner)
class BannerAdmin(TranslatorMediaMixin):
    list_display = (
        "title",
        "subtitle",
    )
    def has_add_permission(self, request):
        if models.Banner.objects.count()>=1:
            return False
        return True



class PlaceGallaryInline(admin.StackedInline):
    model = models.PlaceGallary
    fields = ("image",)
    extra = 1


@admin.register(models.PlaceName)
class PlaceNameAdmin(TranslatorMediaMixin):
    list_display = ("name",)
    inlines = [
        PlaceGallaryInline,
    ]
    search_fields = ("name",)


# Register your models here.

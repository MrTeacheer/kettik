from django.contrib import admin
from common.base.trans_checkbox import (
    TranslatorMediaMixin,
    TranslatorMediaStackedInline,
)
from . import models

# Register your models here.


@admin.register(models.Banner)
class BannerAdmin(TranslatorMediaMixin):
    list_display = (
        "title",
        "subtitle",
        "image",
    )

    def has_add_permission(self, request):
        if models.Banner.objects.count() >= 1:
            return False
        return True


class ArticleExtraInline(TranslatorMediaStackedInline):
    fields = ("text", "image")
    model = models.ArticleExtra
    extra = 1


@admin.register(models.Article)
class ArticleAdmin(TranslatorMediaMixin):
    list_display = (
        "title",
        "image",
    )
    search_fields = ("title",)
    inlines = [
        ArticleExtraInline,
    ]


@admin.register(models.Regions)
class RegionAdmin(TranslatorMediaMixin):
    list_display = ("name",)
    search_fields = ("name",)

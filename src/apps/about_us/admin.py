from django.contrib import admin
from common.base.trans_checkbox import TranslatorMediaMixin
from . import models


@admin.register(models.Banner)
class BannerAdmin(TranslatorMediaMixin):
    list_display = ("title", "image", "subtitle")

    def has_add_permission(self, request):
        if models.Banner.objects.count() >= 1:
            return False
        return True


@admin.register(models.History)
class HistoryAdmin(TranslatorMediaMixin):
    list_display = ("title",)


@admin.register(models.Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("image",)
    list_display_links = ("image",)


@admin.register(models.InDigits)
class InDigitsAdmin(admin.ModelAdmin):
    list_display = (
        "years",
        "amount_tourist",
        "amount_paths",
        "amount_gids",
        "background_image",
    )

    def has_add_permission(self, request):
        if models.InDigits.objects.count() >= 1:
            return False
        return True


@admin.register(models.Team)
class TeamAdmin(TranslatorMediaMixin):
    list_display = ("name", "duty", "image")
    search_fields = ("name", "duty")

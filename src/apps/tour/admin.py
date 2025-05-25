from django.contrib import admin
from . import models
from common.base.trans_checkbox import (
    TranslatorMediaMixin,
    TranslatorMediaStackedInline,
)


@admin.register(models.Banner)
class BannerAdmin(TranslatorMediaMixin):
    list_display = (
        "title",
        "subtitle",
    )


class TourGallaryInline(admin.StackedInline):
    model = models.TourGallary
    fields = ("image",)
    extra = 1


class TourProgramInline(TranslatorMediaStackedInline):
    model = models.TourProgram
    fields = ("image", "day", "title")
    extra = 1


@admin.register(models.Advantages)
class AdvantagesAdmin(TranslatorMediaMixin):
    list_display = ("title",)


@admin.register(models.FAQ)
class FAQAdmin(TranslatorMediaMixin):
    list_display = ("question",)


@admin.register(models.Tour)
class TourAdmin(TranslatorMediaMixin):
    list_display = ("title", "go_date")
    inlines = [TourGallaryInline, TourProgramInline]
    list_filter = [
        "is_active",
        "go_date",
    ]
    search_fields = (
        "title",
        "place",
        "type",
        "difficulty",
        "go_date",
        "duration",
        "price",
    )


class PlacesInline(TranslatorMediaStackedInline):
    model = models.Places
    fields = ("name",)
    extra = 1


@admin.register(models.Country)
class CountryAdmin(TranslatorMediaMixin):
    list_display = ("name",)
    inlines = [
        PlacesInline,
    ]


@admin.register(models.TourType)
class TourTypeAdmin(TranslatorMediaMixin):
    list_display = ("name",)


# Register your models here.

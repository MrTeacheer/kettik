from django.contrib import admin
from . import models
from common.base.trans_checkbox import (
    TranslatorMediaMixin,
    TranslatorMediaStackedInline,
)
from django_celery_beat.admin import (
    CrontabSchedule,
    ClockedSchedule,
    PeriodicTask,
    IntervalSchedule,
    SolarSchedule,
)
from django_summernote.admin import SummernoteInlineModelAdmin
from django_summernote.models import Attachment

admin.site.unregister(CrontabSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(SolarSchedule)
admin.site.unregister(Attachment)


@admin.register(models.Banner)
class BannerAdmin(TranslatorMediaMixin):
    list_display = (
        "title",
        "subtitle",
    )

    def has_add_permission(self, request):
        if models.Banner.objects.count() >= 1:
            return False
        return True


class TourGallaryInline(admin.StackedInline):
    model = models.TourGallary
    fields = ("image",)
    extra = 1


class TourProgramInline(
    SummernoteInlineModelAdmin,
    TranslatorMediaStackedInline,
):
    model = models.TourProgram
    fields = ("image", "day", "text")
    ordering = ("dat",)
    summernote_fields = ("text",)
    extra = 1


@admin.register(models.Advantages)
class AdvantagesAdmin(TranslatorMediaMixin):
    list_display = ("title",)


@admin.register(models.FAQ)
class FAQAdmin(TranslatorMediaMixin):
    list_display = ("question",)


class GoDateTourInline(admin.StackedInline):
    model = models.GoDateTour
    fields = ("go_date",)
    extra = 1


class LivingPlaceTourInline(admin.StackedInline):
    model = models.LivingPlaces
    fields = ("name",)
    extra = 1


@admin.register(models.Tour)
class TourAdmin(TranslatorMediaMixin):
    list_display = ("title",)
    inlines = [
        TourGallaryInline,
        TourProgramInline,
        GoDateTourInline,
        LivingPlaceTourInline,
    ]
    list_filter = [
        "is_active",
    ]
    search_fields = (
        "title",
        # "place",
        "type",
        "difficulty",
        "duration",
        "price",
    )


# class PlacesInline(TranslatorMediaStackedInline):
#     model = models.Places
#     fields = ("name",)
#     extra = 1


# @admin.register(models.Country)
# class CountryAdmin(TranslatorMediaMixin):
#     list_display = ("name",)
#     inlines = [
#         PlacesInline,
#     ]


@admin.register(models.TourType)
class TourTypeAdmin(TranslatorMediaMixin):
    list_display = ("name",)


# Register your models here.

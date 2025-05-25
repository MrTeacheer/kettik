from django.contrib import admin
from common.base.trans_checkbox import TranslatorMediaMixin
from . import models


@admin.register(models.Banner)
class BannerAdmin(TranslatorMediaMixin):
    list_display = ("title", "image", "subtitle")


@admin.register(models.History)
class HistoryAdmin(TranslatorMediaMixin):
    list_display = ("title",)


@admin.register(models.Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("image",)
    list_display_links = ('image',)


@admin.register(models.InDigits)
class InDigitsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Team)
class TeamAdmin(TranslatorMediaMixin):
    list_display = ("name", "phone", "image")
    search_fields = ("name", "phone")

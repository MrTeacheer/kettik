from django.contrib import admin
from common.base.trans_checkbox import TranslatorMediaMixin
from . import models

# Register your models here.


@admin.register(models.Banner)
class BannerAdmin(TranslatorMediaMixin):
    list_display = (
        "title",
        "subtitle",
        "image",
    )


@admin.register(models.Article)
class ArticleAdmin(TranslatorMediaMixin):
    list_display = (
        "title",
        "image",
    )
    search_fields = ("title",)


# Register your models here.

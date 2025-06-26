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
    def has_add_permission(self, request):
        if models.Banner.objects.count()>=1:
            return False
        return True



@admin.register(models.Application)
class ApplAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("email", "name", "phone")


@admin.register(models.GoogleReviews)
class GoogleAdmin(admin.ModelAdmin):
    list_display = ("name", "avatar", "rating")
    search_fields = ("name", "rating")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)


@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("phone", "whatsapp", "telegram", "instagram")

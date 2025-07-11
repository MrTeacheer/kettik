from django.db import models
from common.base.model import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from common.utils.fields import CompressedImageField


class Banner(BaseModel):
    image = CompressedImageField(verbose_name="фото", upload_to="main_page/")
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    subtitle = models.TextField(verbose_name="подзоголовок")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"


class Application(BaseModel):
    name = models.CharField(max_length=500, verbose_name="имя")
    email = models.EmailField(verbose_name="почта")
    phone = PhoneNumberField(verbose_name="номер")
    comment = models.TextField(verbose_name="комент")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class GoogleReviews(BaseModel):
    name = models.CharField(max_length=300)
    avatar = models.URLField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()

    class Meta:
        unique_together = ("name", "created_at")
        verbose_name = "Отзывы с гугла"
        verbose_name_plural = "Отзывы с гугла"


class Contacts(BaseModel):
    phone = PhoneNumberField(verbose_name="номер")
    open_time = models.TimeField(verbose_name="время открытия")
    close_time = models.TimeField(verbose_name="время закрытия")
    email = models.EmailField(verbose_name="почта")
    whatsapp = models.URLField()
    instagram = models.URLField()
    telegram = models.URLField()
    map = models.TextField(verbose_name="карта iframe")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class ImageSlider(BaseModel):
    image = CompressedImageField(verbose_name="фото", upload_to="main_page/")

    class Meta:
        verbose_name = "Слайдер фотографий"
        verbose_name_plural = "Слайдер фотографий"



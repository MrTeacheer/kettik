from django.db import models
from common.base.model import BaseModel
from common.utils.fields import CompressedImageField


class Banner(BaseModel):
    image = CompressedImageField(verbose_name="фото", upload_to="main_page/")
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    subtitle = models.TextField(verbose_name="подзоголовок")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"


class History(BaseModel):
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    text = models.TextField(verbose_name="текст")

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"


class Images(BaseModel):
    image = CompressedImageField(verbose_name="фото", upload_to="about_us/")

    class Meta:
        verbose_name = "Фотки"
        verbose_name_plural = "Фотки"


class InDigits(BaseModel):
    background_image = CompressedImageField(
        verbose_name="заднее фото", upload_to="about_us/", null=True
    )
    years = models.PositiveSmallIntegerField(verbose_name="лет на рынке")
    amount_tourist = models.PositiveIntegerField(
        verbose_name="кол-тво довольных туристов"
    )
    amount_paths = models.PositiveIntegerField(
        verbose_name="кол-тво разных тур-маршрутов по Центральной Азии"
    )
    amount_gids = models.PositiveIntegerField(
        verbose_name="кол-тво профессиональных гидов"
    )

    class Meta:
        verbose_name = "Мы в цифрах"
        verbose_name_plural = "Мы в цифрах"


class Team(BaseModel):
    name = models.CharField(max_length=500, verbose_name="имя фамилие")
    image = CompressedImageField(verbose_name="фото", upload_to="about_us/")
    text = models.TextField(verbose_name="текст")
    duty = models.CharField(verbose_name="должность", null=True)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"

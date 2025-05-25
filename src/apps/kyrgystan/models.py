from django.db import models
from common.base.model import BaseModel


class Banner(BaseModel):
    image = models.ImageField(verbose_name="фото", upload_to="main_page/")
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    subtitle = models.TextField(verbose_name="подзоголовок")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"


class Article(BaseModel):
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    text = models.TextField(verbose_name="описание")
    image = models.ImageField(verbose_name="фото", upload_to="kyrg/")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

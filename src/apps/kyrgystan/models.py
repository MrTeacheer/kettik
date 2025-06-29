from django.db import models
from common.base.model import BaseModel
from common.utils.fields import CompressedImageField
from .choices import RegionsChoices


class Banner(BaseModel):
    image = CompressedImageField(verbose_name="фото", upload_to="main_page/")
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    subtitle = models.TextField(verbose_name="подзоголовок")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"


class Regions(BaseModel):
    text = models.TextField(verbose_name="описание")
    name = models.CharField(choices=RegionsChoices.choices, verbose_name="область")

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class Article(BaseModel):
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    text = models.TextField(verbose_name="описание")
    image = CompressedImageField(verbose_name="фото", upload_to="kyrg/")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ArticleExtra(BaseModel):
    text = models.TextField(verbose_name="описание")
    image = CompressedImageField(verbose_name="фото", upload_to="kyrg/")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="extra")

    class Meta:
        verbose_name = "Статья Допополнение"
        verbose_name_plural = "Статьи Допополнение"

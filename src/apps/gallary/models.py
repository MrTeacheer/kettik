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


class PlaceName(BaseModel):
    name = models.CharField(max_length=500, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Места"
        verbose_name_plural = "Места"


class PlaceGallary(BaseModel):
    image = CompressedImageField(verbose_name="фото", upload_to="gallary/")
    place = models.ForeignKey(
        PlaceName, on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

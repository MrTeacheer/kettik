from django.db import models
from common.base.model import BaseModel


class Banner(BaseModel):
    image = models.ImageField(verbose_name="фото", upload_to="main_page/")
    title = models.CharField(max_length=500, verbose_name="зоголовок")
    subtitle = models.TextField(verbose_name="подзоголовок")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"


class Tour(BaseModel):
    photo_video = models.FileField(verbose_name="фото или видео", upload_to="tour/")
    title = models.CharField(verbose_name="зоголовок", max_length=500)
    price = models.PositiveIntegerField(verbose_name="цена")
    go_date = models.DateField(verbose_name="Дата выезда")
    duration = models.PositiveSmallIntegerField(verbose_name="Длительность")
    difficulty = models.CharField(verbose_name="Сложность", max_length=500)
    type = models.ForeignKey(
        "TourType", verbose_name="тип", related_name="tours", on_delete=models.PROTECT
    )
    place = models.ForeignKey(
        "Places", verbose_name="место", on_delete=models.PROTECT, related_name="tours"
    )
    map = models.TextField(verbose_name="карта-iframe")
    advantages = models.ManyToManyField(
        "Advantages", verbose_name="Что включено в стоимость", related_name="adv_tours"
    )
    disadvantages = models.ManyToManyField(
        "Advantages",
        verbose_name="Что не включено в стоимость",
        related_name="dis_tours",
    )
    is_active = models.BooleanField(default=True, verbose_name="активный?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class TourType(BaseModel):
    name = models.CharField(verbose_name="тип", max_length=500, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип Тура"
        verbose_name_plural = "Типы Тура"


class TourGallary(BaseModel):
    image = models.ImageField(verbose_name="фото", upload_to="tour/")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"


class TourProgram(BaseModel):
    image = models.ImageField(verbose_name="фото", upload_to="tour/")
    day = models.PositiveSmallIntegerField(verbose_name="день")
    title = models.CharField(verbose_name="зоголовок", max_length=500)
    text = models.TextField(verbose_name="описание")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="programs")

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программа"


class Advantages(BaseModel):
    title = models.CharField(verbose_name="зоголовок", max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Удобство туров"
        verbose_name_plural = "Удобство туров"


class FAQ(BaseModel):
    question = models.TextField(verbose_name="вопрос")
    answer = models.TextField(verbose_name="ответ")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"


class Country(BaseModel):
    name = models.CharField(max_length=500, verbose_name="страна")

    class Meta:
        verbose_name = "Страны"
        verbose_name_plural = "Страны"


class Places(BaseModel):
    name = models.CharField(max_length=500, verbose_name="место")
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name="страна", related_name="places"
    )

    def __str__(self):
        return f"{self.country.name}-{self.name}"

    class Meta:
        verbose_name = "Места"
        verbose_name_plural = "Места"

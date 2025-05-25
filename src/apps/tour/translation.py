from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Banner)
class BannerTrans(TranslationOptions):
    fields = ("title", "subtitle")


@register(models.Tour)
class TourTrans(TranslationOptions):
    fields = ("title", "difficulty", "type")


@register(models.TourProgram)
class TourProgramTrans(TranslationOptions):
    fields = ("title", "text")


@register(models.Advantages)
class AdvantagesTrans(TranslationOptions):
    fields = ("title",)


@register(models.FAQ)
class FAQtrans(TranslationOptions):
    fields = ("question", "answer")


@register(models.Country)
class Countrytrans(TranslationOptions):
    fields = ("name",)


@register(models.Places)
class Placestrans(TranslationOptions):
    fields = ("name",)


@register(models.TourType)
class TourTypetrans(TranslationOptions):
    fields = ("name",)

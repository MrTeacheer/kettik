from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Banner)
class BannerTrans(TranslationOptions):
    fields = ("title", "subtitle")

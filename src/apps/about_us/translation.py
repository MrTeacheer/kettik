from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Banner)
class BannerTrans(TranslationOptions):
    fields = ("title", "subtitle")


@register(models.History)
class HistoryTrans(TranslationOptions):
    fields = ("title", "text")


@register(models.Team)
class TeamTrans(TranslationOptions):
    fields = ("name", "text", "duty")

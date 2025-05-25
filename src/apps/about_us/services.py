from . import models
from common.base.service import BaseService


class BannerService(BaseService[models.Banner]):
    model = models.Banner


class HistoryService(BaseService[models.History]):
    model = models.History


class ImagesService(BaseService[models.Images]):
    model = models.Images

class InDigitsService(BaseService[models.InDigits]):
    model = models.InDigits


class TeamService(BaseService[models.Team]):
    model = models.Team
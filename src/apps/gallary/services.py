from . import models
from common.base.service import BaseService


class BannerService(BaseService[models.Banner]):
    model = models.Banner


class PlaceService(BaseService[models.PlaceName]):
    model = models.PlaceName

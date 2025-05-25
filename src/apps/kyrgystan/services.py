from . import models
from common.base.service import BaseService


class BannerService(BaseService[models.Banner]):
    model = models.Banner


class ArticleService(BaseService[models.Article]):
    model = models.Article

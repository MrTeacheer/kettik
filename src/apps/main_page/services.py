from common.base.service import BaseService
from . import models


class GoogleReviewsService(BaseService[models.GoogleReviews]):
    model = models.GoogleReviews


class BannerService(BaseService[models.Banner]):
    model = models.Banner


class ApplicationService(BaseService[models.Application]):
    model = models.Application


class ContactService(BaseService[models.Contacts]):
    model = models.Contacts

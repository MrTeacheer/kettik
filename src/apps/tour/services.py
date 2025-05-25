from . import models
from common.base.service import BaseService


class BannerService(BaseService[models.Banner]):
    model = models.Banner


class TourService(BaseService[models.Tour]):
    model = models.Tour

    @classmethod
    def get_filtered_tours(cls, max_days, min_days):
        if max_days and min_days:
            return cls.model.objects.filter(
                is_active=True, duration__lte=max_days, duration__gte=min_days
            ).order_by("-created_at")
        elif max_days and not min_days:
            return cls.model.objects.filter(
                is_active=True, duration__lte=max_days
            ).order_by("-created_at")

        elif min_days and not max_days:
            return cls.model.objects.filter(
                is_active=True, duration__gte=min_days
            ).order_by("-created_at")


class FAQService(BaseService[models.FAQ]):
    model = models.FAQ

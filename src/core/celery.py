import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "fetch_google_reviews_daily": {
        "task": "apps.main_page.tasks.fetch_google_reviews",
        "schedule": crontab(hour=0, minute=0),  # каждый день в 00:00
    }
}
app.autodiscover_tasks()

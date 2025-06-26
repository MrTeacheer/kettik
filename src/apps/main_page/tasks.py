from celery import shared_task
import requests
import json
from django.utils.dateparse import parse_datetime
from .models import GoogleReviews
from django.conf import settings
from common.utils.logger import logger


@shared_task
def fetch_google_reviews():
    url = "https://google.serper.dev/reviews"
    headers = {"X-API-KEY": settings.XAPI_KEY, "Content-Type": "application/json"}

    payload = json.dumps({"placeId": settings.PLACE_ID, "sortBy": "newest"})

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code != 200:
        print(f"Failed to fetch reviews: {response.status_code}")
        return

    data = response.json()
    reviews_data = data.get("reviews", [])
    reviews = []

    for review in reviews_data:
        user = review.get("user", {})
        reviews.append(
            GoogleReviews(
                name=user.get("name"),
                avatar=user.get("thumbnail"),
                rating=review.get("rating"),
                text=review.get("snippet"),
                created_at=parse_datetime(review.get("isoDate")),
            )
        )

    GoogleReviews.objects.bulk_create(reviews, ignore_conflicts=True)
    logger.info("GOOGLE REVIEWS FETCH SUCCESS")

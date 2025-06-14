import json
import requests
from django.core.management.base import BaseCommand
from common.utils.logger import logger
from apps.main_page.models import GoogleReviews
from django.conf import settings

class Command(BaseCommand):
    help = "Fetch reviews from Serper API"

    def handle(self, *args, **options):
        page_tokens = []
        next_page = None
        page_number = 1
        reviews = []
        count_reviews = 0
        while True:
            url = "https://google.serper.dev/reviews"
            payload = json.dumps(
                {
                    "placeId": settings.PLACE_ID,
                    "sortBy": "newest",
                    "nextPageToken": next_page,
                }
            )
            headers = {
                "X-API-KEY": settings.XAPI_KEY,
                "Content-Type": "application/json",
            }

            response = requests.post(url, headers=headers, data=payload)
            json_response = response.json()

            if response.status_code == 200:
                if json_response["nextPageToken"] not in page_tokens:
                    count_reviews += len(json_response["reviews"])
                    for review in json_response["reviews"]:
                        reviews.append(
                            GoogleReviews(
                                name=review.get("user", {}).get("name"),
                                avatar=review.get("user", {}).get("thumbnail"),
                                rating=review.get("rating"),
                                text=review.get("snippet"),
                                created_at=review.get("isoDate"),
                            )
                        )
                    logger.info(page_number)
                    page_tokens.append(json_response["nextPageToken"])
                    next_page = json_response["nextPageToken"]
                    page_number += 1
                else:
                    self.stdout.write(self.style.SUCCESS("FINISH:"))
                    self.stdout.write(self.style.SUCCESS(count_reviews))
                    break
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed to fetch reviews, status code: {response.status_code}"
                    )
                )
                self.stdout.write(response.text)
                break
        GoogleReviews.objects.bulk_create(reviews,ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS("SAVED TO DB"))

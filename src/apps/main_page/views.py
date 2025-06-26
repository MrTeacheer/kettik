from common.base.generics import (
    CustomListAPIView,
    CustomRetieveAPIView,
    CustomCreateAPIView,
)
from . import services, serializers, swagger
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings


@swagger.reviews_schema
class GoogleReviewsView(CustomListAPIView):
    serializer_class = serializers.GoogleReviewsSerializer
    service_class = services.GoogleReviewsService
    order_by_ = ["-rating", "-created_at"]


@swagger.banner_schema
class BannerView(CustomRetieveAPIView):
    serializer_class = serializers.BannerSerializer
    service_class = services.BannerService


@swagger.application_schema
class ApplicationView(CustomCreateAPIView):
    serializer_class = serializers.ApplicationSerializer
    post_serializer_class = serializers.ApplicationCreateSerializer
    service_class = services.ApplicationService

    def create(self, request, *args, **kwargs):
        serializer = self.post_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        created_obj = self.service_class.create(**serializer.validated_data)

        text = f"Новая Заявка:\n Имя: {created_obj.name}\n Коментарий: {created_obj.comment}\n Почта: {created_obj.email}\n Номер: {created_obj.phone}"

        bot_token = settings.BOT_TOKEN
        chat_id = settings.CHAT_ID

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
        }

        requests.post(url, data=payload)
        serializer = self.get_serializer(created_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@swagger.contact_schema
class ContactsView(CustomRetieveAPIView):
    serializer_class = serializers.ContactsSerializer
    service_class = services.ContactService

from rest_framework import serializers
from . import models
from phonenumber_field.serializerfields import PhoneNumberField


class GoogleReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GoogleReviews
        fields = (
            "id",
            "name",
            "avatar",
            "rating",
            "text",
            "created_at",
        )


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Banner
        fields = (
            "image",
            "title",
            "subtitle",
        )


class ImageSliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ImageSlider
        fields = (
            "id",
            "image",
        )


class ApplicationCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = PhoneNumberField()
    comment = serializers.CharField()


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Application
        fields = (
            "name",
            "email",
            "phone",
            "comment",
        )


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contacts
        fields = (
            "phone",
            "open_time",
            "close_time",
            "email",
            "whatsapp",
            "instagram",
            "telegram",
            "map",
        )

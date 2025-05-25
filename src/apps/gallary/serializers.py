from . import models
from rest_framework import serializers


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Banner
        fields = (
            "image",
            "title",
            "subtitle",
        )


class PlaceGallarySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlaceGallary
        fields = (
            "id",
            "image",
        )


class PlaceSerializer(serializers.ModelSerializer):
    images = PlaceGallarySerializer(many=True)

    class Meta:
        model = models.PlaceName
        fields = (
            "id",
            "name",
            "images",
        )

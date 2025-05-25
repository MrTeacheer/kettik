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


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.History
        fields = ("title", "text")


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Images
        fields = ("id", "image")


class InDigitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InDigits
        fields = (
            "years",
            "amount_tourist",
            "amount_paths",
            "amount_gids",
        )


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Team
        fields = (
            "id",
            "name",
            "image",
            "text",
            "phone",
        )

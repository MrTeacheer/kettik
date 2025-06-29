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


class ArticleExtraSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ArticleExtra
        fields = ("id", "text", "image")


class ArticleSerializer(serializers.ModelSerializer):
    extra = ArticleExtraSerializer(many=True)

    class Meta:
        model = models.Article
        fields = ("id", "image", "title", "text", "created_at", "extra")


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Regions
        fields = ("id", "name", "text")

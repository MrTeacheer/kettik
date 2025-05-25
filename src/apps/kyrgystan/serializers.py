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


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = (
            "id",
            "image",
            "title",
            "text",
            "created_at",
        )

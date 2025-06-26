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


class TourSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        model = models.Tour
        fields = (
            "id",
            "video",
            "image",
            "title",
            "price",
        )

    def get_image(self, obj):
        return self.validate_photo_video(obj, "jpg", "jpeg", "png")

    def get_video(self, obj):
        return self.validate_photo_video(obj, "mp4")

    def validate_photo_video(self, obj, *ext):
        request = self.context["request"]
        if obj.photo_video.url.endswith(ext):
            return request.build_absolute_uri(obj.photo_video.url)
        return None


class AdvantagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Advantages
        fields = ("id", "title")


class TourImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TourGallary
        fields = ("id", "image")


class TourProgramsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TourProgram
        fields = (
            "id",
            "image",
            "day",
            "text",
        )


class GoDatesTour(serializers.ModelSerializer):
    class Meta:
        model = models.GoDateTour
        fields = (
            "id",
            "go_date",
        )


class LivingPlacesTour(serializers.ModelSerializer):
    class Meta:
        model = models.LivingPlaces
        fields = (
            "id",
            "name",
        )


class TourDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    type = serializers.CharField(source="type.name")
    disadvantages = AdvantagesSerializer(many=True)
    advantages = AdvantagesSerializer(many=True)
    images = TourImagesSerializer(many=True)
    programs = TourProgramsSerializer(many=True)
    go_dates = GoDatesTour(many=True)
    living_places = LivingPlacesTour(many=True)

    class Meta:
        model = models.Tour
        fields = (
            "video",
            "image",
            "title",
            "price",
            "duration",
            "difficulty",
            "type",
            "map",
            "advantages",
            "disadvantages",
            "images",
            "programs",
            "go_dates",
            "living_places",
        )

    def get_image(self, obj):
        return self.validate_photo_video(obj, "jpg", "jpeg", "png")

    def get_video(self, obj):
        return self.validate_photo_video(obj, "mp4")

    def validate_photo_video(self, obj, *ext):
        request = self.context["request"]
        if obj.photo_video.url.endswith(ext):
            return request.build_absolute_uri(obj.photo_video.url)
        return None


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FAQ
        fields = ("id", "question", "answer")

from rest_framework import serializers


class BaseValidateSerializer(serializers.Serializer):

    @property
    def get_filters(self):
        filters = {}
        return filters

    @property
    def get_excludes(self):
        excludes = {}
        return excludes

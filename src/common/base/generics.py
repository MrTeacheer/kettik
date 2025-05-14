from rest_framework.generics import GenericAPIView
from common.base import mixins


class CustomGenericAPIView(GenericAPIView):
    serializer_class = None
    post_serializer_class = None
    put_serializer_class = None
    service_class = None
    validate_serializer_class = None
    prefetch_: list[str] = []
    select_: list[str] = []
    order_by_: list[str] = []

    def get_queryset(self, excludes={}, *args, **filters):
        queryset = self.service_class.list(
            select_=self.select_,
            prefetch_=self.prefetch_,
            order_by_=self.order_by_,
            excludes=excludes,
            **filters
        )
        return queryset

    def get_object(self, *args, **kwargs):
        obj = self.service_class.retriev(
            select_=self.select_, prefetch_=self.prefetch_, **kwargs
        )
        return obj


class CustomListCreateAPIView(
    mixins.ListModelMixin, mixins.CreateModelMixin, CustomGenericAPIView
):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomRetrievUpdageDestroyAPIView(
    mixins.RetrievModelMixin,
    mixins.UpdateModelMixin,
    mixins.DeleteModelMixin,
    CustomGenericAPIView,
):

    def get(self, request, *args, **kwargs):
        return self.retriev(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomListAPIView(mixins.ListModelMixin, CustomGenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomCreateAPIView(mixins.CreateModelMixin, CustomGenericAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomRetieveAPIView(mixins.RetrievModelMixin, CustomGenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.retriev(request, *args, **kwargs)


class CustomUpdateAPIView(mixins.UpdateModelMixin, CustomGenericAPIView):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

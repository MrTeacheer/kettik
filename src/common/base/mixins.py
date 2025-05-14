from rest_framework import status
from rest_framework.response import Response


class ListModelMixin:

    def list(self, request, *arsg, **kwargs):
        queryset = self.get_queryset()

        if self.validate_serializer_class:
            val_serializer = self.validate_serializer_class(
                data=request.query_params, partial=True
            )
            val_serializer.is_valid(raise_exception=True)
            filters = val_serializer.get_filters
            excludes = val_serializer.get_excludes
            queryset = self.get_queryset(excludes, **filters)

        page = self.paginate_queryset(queryset)
        if page:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateModelMixin:

    def create(self, request, *args, **kwargs):
        serializer = self.post_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        created_obj = self.service_class.create(**serializer.validated_data)
        serializer = self.get_serializer(created_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class RetrievModelMixin:

    def retriev(self, request, *args, **kwargs):
        if self.validate_serializer_class:
            val_serializer = self.validate_serializer_class(
                data=request.query_params, partial=True
            )
            val_serializer.is_valid(raise_exception=True)
            kwargs.update(val_serializer.get_filters)
        obj = self.get_object(**kwargs)
        serializer = self.get_serializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UpdateModelMixin:

    def update(self, request, *args, **kwargs):
        return self.base_update(
            request=request,
            partial=False,
            update_method=self.service_class.update,
            **kwargs
        )

    def partial_update(self, request, *args, **kwargs):
        return self.base_update(
            request=request,
            partial=True,
            update_method=self.service_class.partial_update,
            **kwargs
        )

    def base_update(self, request, partial, update_method, **kwargs):
        obj = self.get_object(**kwargs)
        serializer = self.put_serializer_class(data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        updated_obj = update_method(obj, **serializer.validated_data)
        serializer = self.get_serializer(updated_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DeleteModelMixin:

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object(**kwargs)
        self.service_class.delete(obj)
        return Response(data="instance is deleted", status=status.HTTP_204_NO_CONTENT)

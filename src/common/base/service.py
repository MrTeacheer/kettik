from typing import Generic, Type, TypeVar
from django.db.models import Model


T = TypeVar("T", bound=Model)


class BaseService(Generic[T]):
    model: Type[T]

    @classmethod
    def list(cls, select_=[], prefetch_=[], order_by_=[], excludes={}, **filters):
        queryset = (
            cls.model.objects.filter(**filters)
            .select_related(*select_)
            .prefetch_related(*prefetch_)
            .order_by(*order_by_)
            .exclude(**excludes)
        )
        return queryset

    @classmethod
    def create(cls, **kwargs):
        obj = cls.model.objects.create(**kwargs)
        return obj

    @classmethod
    def retriev(cls, select_=[], prefetch_=[], **kwargs):
        obj = (
            cls.model.objects.filter(**kwargs)
            .select_related(*select_)
            .prefetch_related(*prefetch_)
            .first()
        )
        return obj

    @classmethod
    def update(cls, obj: Model, **kwargs):
        for field, value in kwargs.items():
            setattr(obj, field, value)
        obj.save(update_fields=kwargs.keys())
        return obj

    @classmethod
    def partial_update(cls, obj: Model, **kwargs):
        return cls.update(obj, **kwargs)

    @classmethod
    def delete(cls, obj: Model):
        obj.delete()

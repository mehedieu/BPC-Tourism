from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Destination, DestinationCategory
from .serializers import (
    DestinationSerializer,
    DestinationCategorySerializer,
)


class DestinationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DestinationSerializer
    lookup_field = "slug"

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["division", "district", "category__slug"]
    search_fields = ["name_en", "name_bn", "district", "division"]
    ordering_fields = ["name_en", "created_at"]
    ordering = ["name_en"]

    def get_queryset(self):
        return (
            Destination.objects
            .filter(is_published=True)
            .select_related("category")
            .prefetch_related("images")
        )


class DestinationCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DestinationCategory.objects.all().order_by("name_en")
    serializer_class = DestinationCategorySerializer
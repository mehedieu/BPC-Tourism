from rest_framework import serializers
from .models import (
    Destination,
    DestinationCategory,
    DestinationImage,
)


class DestinationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationCategory
        fields = ["id", "name_en", "name_bn", "slug"]


class DestinationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = [
            "id",
            "image",
            "alt_text_en",
            "alt_text_bn",
            "is_primary",
        ]


class DestinationSerializer(serializers.ModelSerializer):
    category = DestinationCategorySerializer(read_only=True)
    images = DestinationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = [
            "id",
            "name_en",
            "name_bn",
            "slug",
            "category",
            "description_en",
            "description_bn",
            "division",
            "district",
            "address",
            "latitude",
            "longitude",
            "opening_information",
            "travel_information_en",
            "travel_information_bn",
            "images",
        ]
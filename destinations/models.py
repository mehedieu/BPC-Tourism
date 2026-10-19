from django.db import models
from django.utils.text import slugify


class DestinationCategory(models.Model):
    name_en = models.CharField(max_length=100)
    name_bn = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name_en


class Destination(models.Model):
    category = models.ForeignKey(
        DestinationCategory,
        on_delete=models.PROTECT,
        related_name="destinations",
    )
    name_en = models.CharField(max_length=200)
    name_bn = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description_en = models.TextField()
    description_bn = models.TextField()
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    opening_information = models.TextField(blank=True)
    travel_information_en = models.TextField(blank=True)
    travel_information_bn = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name_en"]

    def __str__(self):
        return self.name_en


class DestinationImage(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="destinations/")
    alt_text_en = models.CharField(max_length=200, blank=True)
    alt_text_bn = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.destination.name_en} image"
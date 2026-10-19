from django.contrib import admin
from .models import Destination, DestinationCategory, DestinationImage


class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 1


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = (
        "name_en",
        "district",
        "division",
        "is_published",
    )
    list_filter = (
        "division",
        "district",
        "category",
        "is_published",
    )
    search_fields = ("name_en", "name_bn", "district")
    prepopulated_fields = {"slug": ("name_en",)}
    inlines = [DestinationImageInline]


@admin.register(DestinationCategory)
class DestinationCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_en", "name_bn", "slug")
from django.contrib import admin
from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'price',
        'duration',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
        'location',
    )

    search_fields = (
        'name',
        'location',
        'description',
    )

    ordering = (
        '-created_at',
    )
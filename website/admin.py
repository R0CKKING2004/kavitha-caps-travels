from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'destination',
        'travel_date',
        'travellers',
        'vehicle',
        'created_at',
    )

    list_filter = (
        'vehicle',
        'travel_date',
        'created_at',
    )

    search_fields = (
        'name',
        'phone',
        'email',
        'destination',
        'message',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    list_per_page = 20
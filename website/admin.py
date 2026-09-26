from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'email',
        'destination',
        'travel_date',
        'travellers',
        'vehicle',
        'created_at',
    )

    list_filter = (
        'vehicle',
        'travel_date',
        'destination',
        'created_at',
    )

    search_fields = (
        'name',
        'phone',
        'email',
        'destination',
        'message',
    )

    date_hierarchy = 'travel_date'

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'created_at',
    )

    fieldsets = (
        (
            'Customer Information',
            {
                'fields': (
                    'name',
                    'phone',
                    'email',
                )
            }
        ),
        (
            'Travel Information',
            {
                'fields': (
                    'destination',
                    'travel_date',
                    'travellers',
                    'vehicle',
                )
            }
        ),
        (
            'Customer Message',
            {
                'fields': (
                    'message',
                )
            }
        ),
        (
            'System Information',
            {
                'fields': (
                    'created_at',
                )
            }
        ),
    )
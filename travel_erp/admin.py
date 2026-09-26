from django.contrib import admin
from .models import Customer, Booking, Vehicle, Payment, Expense


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')
    ordering = ('-created_at',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'package',
        'travel_date',
        'travellers',
        'vehicle',
        'total_amount',
        'advance_amount',
        'balance_amount',
        'booking_status',
        'payment_status',
    )

    list_filter = (
        'booking_status',
        'payment_status',
        'vehicle',
        'travel_date',
    )

    search_fields = (
        'customer__name',
        'customer__phone',
        'package__name',
    )

    date_hierarchy = 'travel_date'


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle_number',
        'vehicle_type',
        'model',
        'capacity',
        'driver_name',
        'driver_phone',
        'is_available',
    )

    list_filter = (
        'vehicle_type',
        'is_available',
    )

    search_fields = (
        'vehicle_number',
        'driver_name',
        'driver_phone',
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'booking',
        'amount',
        'payment_method',
        'payment_date',
        'reference_number',
    )

    list_filter = (
        'payment_method',
        'payment_date',
    )

    search_fields = (
        'booking__customer__name',
        'reference_number',
    )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'amount',
        'expense_date',
        'created_at',
    )

    list_filter = (
        'category',
        'expense_date',
    )

    search_fields = (
        'title',
        'description',
    )
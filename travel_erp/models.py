from django.db import models
from packages.models import Package


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Booking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    PAYMENT_CHOICES = [
        ('Pending', 'Pending'),
        ('Partial', 'Partial'),
        ('Paid', 'Paid'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bookings'
    )

    travel_date = models.DateField()
    return_date = models.DateField(
        null=True,
        blank=True
    )

    travellers = models.PositiveIntegerField(default=1)

    vehicle = models.CharField(
        max_length=50,
        choices=[
            ('Car', 'Car'),
            ('Tempo Traveller', 'Tempo Traveller'),
            ('Tourist Bus', 'Tourist Bus'),
        ]
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    advance_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    balance_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    booking_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='Pending'
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.package}"


class Vehicle(models.Model):

    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Tempo Traveller', 'Tempo Traveller'),
        ('Tourist Bus', 'Tourist Bus'),
    ]

    vehicle_number = models.CharField(
        max_length=20,
        unique=True
    )

    vehicle_type = models.CharField(
        max_length=50,
        choices=VEHICLE_TYPES
    )

    model = models.CharField(
        max_length=100,
        blank=True
    )

    capacity = models.PositiveIntegerField()

    driver_name = models.CharField(
        max_length=100,
        blank=True
    )

    driver_phone = models.CharField(
        max_length=15,
        blank=True
    )

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.vehicle_number


class Payment(models.Model):

    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHODS
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    reference_number = models.CharField(
        max_length=100,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.booking} - ₹{self.amount}"


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('Fuel', 'Fuel'),
        ('Maintenance', 'Maintenance'),
        ('Salary', 'Salary'),
        ('Office', 'Office'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        max_length=150
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    expense_date = models.DateField()

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"
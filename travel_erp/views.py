from decimal import Decimal

from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Customer,
    Booking,
    Vehicle,
    Payment,
    Expense,
)

from packages.models import Package


# ============================================================
# DASHBOARD
# ============================================================

def dashboard(request):

    # -------------------------
    # BASIC COUNTS
    # -------------------------

    total_customers = Customer.objects.count()

    total_packages = Package.objects.count()

    total_bookings = Booking.objects.count()

    total_vehicles = Vehicle.objects.count()


    # -------------------------
    # FINANCIAL SUMMARY
    # -------------------------

    total_payments = (
        Payment.objects.aggregate(
            total=Sum("amount")
        )["total"]
        or Decimal("0")
    )

    total_expenses = (
        Expense.objects.aggregate(
            total=Sum("amount")
        )["total"]
        or Decimal("0")
    )

    net_amount = total_payments - total_expenses


    # -------------------------
    # BOOKING STATUS
    # -------------------------

    pending_bookings = Booking.objects.filter(
        booking_status="Pending"
    ).count()

    confirmed_bookings = Booking.objects.filter(
        booking_status="Confirmed"
    ).count()

    completed_bookings = Booking.objects.filter(
        booking_status="Completed"
    ).count()

    cancelled_bookings = Booking.objects.filter(
        booking_status="Cancelled"
    ).count()


    # -------------------------
    # RECENT BOOKINGS
    # -------------------------

    recent_bookings = Booking.objects.select_related(
        "customer",
        "package"
    ).order_by("-id")[:10]


    # -------------------------
    # RECENT PAYMENTS
    # -------------------------

    recent_payments = Payment.objects.select_related(
        "booking",
        "booking__customer"
    ).order_by("-id")[:5]


    # -------------------------
    # RECENT EXPENSES
    # -------------------------

    recent_expenses = Expense.objects.order_by(
        "-id"
    )[:5]


    # -------------------------
    # CONTEXT
    # -------------------------

    context = {

        "total_customers": total_customers,

        "total_packages": total_packages,

        "total_bookings": total_bookings,

        "total_vehicles": total_vehicles,

        "total_payments": total_payments,

        "total_expenses": total_expenses,

        "net_amount": net_amount,

        "pending_bookings": pending_bookings,

        "confirmed_bookings": confirmed_bookings,

        "completed_bookings": completed_bookings,

        "cancelled_bookings": cancelled_bookings,

        "recent_bookings": recent_bookings,

        "recent_payments": recent_payments,

        "recent_expenses": recent_expenses,
    }


    return render(
        request,
        "travel_erp/dashboard.html",
        context
    )


# ============================================================
# CUSTOMERS
# ============================================================

def customers(request):

    customer_list = Customer.objects.order_by("-id")

    return render(
        request,
        "travel_erp/customers.html",
        {
            "customers": customer_list
        }
    )


def add_customer(request):

    if request.method == "POST":

        Customer.objects.create(
            name=request.POST.get(
                "name",
                ""
            ).strip(),

            phone=request.POST.get(
                "phone",
                ""
            ).strip(),

            email=request.POST.get(
                "email",
                ""
            ).strip(),

            address=request.POST.get(
                "address",
                ""
            ).strip(),
        )

        messages.success(
            request,
            "Customer added successfully."
        )

        return redirect("erp_customers")

    return render(
        request,
        "travel_erp/customer_form.html"
    )


def edit_customer(request, customer_id):

    customer = get_object_or_404(
        Customer,
        id=customer_id
    )

    if request.method == "POST":

        customer.name = request.POST.get(
            "name",
            ""
        ).strip()

        customer.phone = request.POST.get(
            "phone",
            ""
        ).strip()

        customer.email = request.POST.get(
            "email",
            ""
        ).strip()

        customer.address = request.POST.get(
            "address",
            ""
        ).strip()

        customer.save()

        messages.success(
            request,
            "Customer updated successfully."
        )

        return redirect("erp_customers")

    return render(
        request,
        "travel_erp/customer_form.html",
        {
            "customer": customer
        }
    )


def delete_customer(request, customer_id):

    customer = get_object_or_404(
        Customer,
        id=customer_id
    )

    customer.delete()

    messages.success(
        request,
        "Customer deleted successfully."
    )

    return redirect("erp_customers")


# ============================================================
# PACKAGES
# ============================================================

def packages(request):

    package_list = Package.objects.order_by("-id")

    return render(
        request,
        "travel_erp/packages.html",
        {
            "packages": package_list
        }
    )


def add_package(request):

    if request.method == "POST":

        Package.objects.create(
            name=request.POST.get(
                "name",
                ""
            ).strip(),

            location=request.POST.get(
                "location",
                ""
            ).strip(),

            description=request.POST.get(
                "description",
                ""
            ).strip(),

            price=request.POST.get(
                "price",
                0
            ),

            duration=request.POST.get(
                "duration",
                ""
            ).strip(),

            image=request.FILES.get("image"),

            is_active=(
                request.POST.get(
                    "is_active"
                ) == "on"
            ),
        )

        messages.success(
            request,
            "Package added successfully."
        )

        return redirect("erp_packages")

    return render(
        request,
        "travel_erp/package_form.html"
    )


def edit_package(request, package_id):

    package = get_object_or_404(
        Package,
        id=package_id
    )

    if request.method == "POST":

        package.name = request.POST.get(
            "name",
            ""
        ).strip()

        package.location = request.POST.get(
            "location",
            ""
        ).strip()

        package.description = request.POST.get(
            "description",
            ""
        ).strip()

        package.price = request.POST.get(
            "price",
            0
        )

        package.duration = request.POST.get(
            "duration",
            ""
        ).strip()

        if request.FILES.get("image"):
            package.image = request.FILES.get(
                "image"
            )

        package.is_active = (
            request.POST.get(
                "is_active"
            ) == "on"
        )

        package.save()

        messages.success(
            request,
            "Package updated successfully."
        )

        return redirect("erp_packages")

    return render(
        request,
        "travel_erp/package_form.html",
        {
            "package": package
        }
    )


def delete_package(request, package_id):

    package = get_object_or_404(
        Package,
        id=package_id
    )

    package.delete()

    messages.success(
        request,
        "Package deleted successfully."
    )

    return redirect("erp_packages")


def toggle_package(request, package_id):

    package = get_object_or_404(
        Package,
        id=package_id
    )

    package.is_active = not package.is_active

    package.save()

    return redirect("erp_packages")


# ============================================================
# BOOKINGS
# ============================================================

def bookings(request):

    booking_list = Booking.objects.select_related(
        "customer",
        "package"
    ).order_by("-id")

    return render(
        request,
        "travel_erp/bookings.html",
        {
            "bookings": booking_list
        }
    )


def add_booking(request):

    customers_list = Customer.objects.order_by(
        "name"
    )

    packages_list = Package.objects.filter(
        is_active=True
    ).order_by("name")

    if request.method == "POST":

        total_amount = Decimal(
            request.POST.get(
                "total_amount",
                "0"
            ) or "0"
        )

        advance_amount = Decimal(
            request.POST.get(
                "advance_amount",
                "0"
            ) or "0"
        )

        balance_amount = (
            total_amount - advance_amount
        )

        Booking.objects.create(

            customer_id=request.POST.get(
                "customer"
            ),

            package_id=request.POST.get(
                "package"
            ) or None,

            travel_date=request.POST.get(
                "travel_date"
            ),

            return_date=request.POST.get(
                "return_date"
            ) or None,

            travellers=request.POST.get(
                "travellers",
                1
            ),

            vehicle=request.POST.get(
                "vehicle"
            ),

            total_amount=total_amount,

            advance_amount=advance_amount,

            balance_amount=balance_amount,

            booking_status=request.POST.get(
                "booking_status",
                "Pending"
            ),

            payment_status=request.POST.get(
                "payment_status",
                "Pending"
            ),

            notes=request.POST.get(
                "notes",
                ""
            ).strip(),
        )

        messages.success(
            request,
            "Booking added successfully."
        )

        return redirect("erp_bookings")

    return render(
        request,
        "travel_erp/booking_form.html",
        {
            "customers": customers_list,
            "packages": packages_list,
        }
    )


def edit_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    customers_list = Customer.objects.order_by(
        "name"
    )

    packages_list = Package.objects.filter(
        is_active=True
    ).order_by("name")

    if request.method == "POST":

        booking.customer_id = request.POST.get(
            "customer"
        )

        booking.package_id = request.POST.get(
            "package"
        ) or None

        booking.travel_date = request.POST.get(
            "travel_date"
        )

        booking.return_date = request.POST.get(
            "return_date"
        ) or None

        booking.travellers = request.POST.get(
            "travellers",
            1
        )

        booking.vehicle = request.POST.get(
            "vehicle"
        )

        booking.total_amount = Decimal(
            request.POST.get(
                "total_amount",
                "0"
            ) or "0"
        )

        booking.advance_amount = Decimal(
            request.POST.get(
                "advance_amount",
                "0"
            ) or "0"
        )

        booking.balance_amount = (
            booking.total_amount
            - booking.advance_amount
        )

        booking.booking_status = request.POST.get(
            "booking_status",
            "Pending"
        )

        booking.payment_status = request.POST.get(
            "payment_status",
            "Pending"
        )

        booking.notes = request.POST.get(
            "notes",
            ""
        ).strip()

        booking.save()

        messages.success(
            request,
            "Booking updated successfully."
        )

        return redirect("erp_bookings")

    return render(
        request,
        "travel_erp/booking_form.html",
        {
            "booking": booking,
            "customers": customers_list,
            "packages": packages_list,
        }
    )


def delete_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.delete()

    messages.success(
        request,
        "Booking deleted successfully."
    )

    return redirect("erp_bookings")


# ============================================================
# VEHICLES
# ============================================================

def vehicles(request):

    vehicle_list = Vehicle.objects.order_by("-id")

    return render(
        request,
        "travel_erp/vehicles.html",
        {
            "vehicles": vehicle_list
        }
    )


def add_vehicle(request):

    if request.method == "POST":

        Vehicle.objects.create(

            vehicle_number=request.POST.get(
                "vehicle_number",
                ""
            ).strip(),

            vehicle_type=request.POST.get(
                "vehicle_type"
            ),

            model=request.POST.get(
                "model",
                ""
            ).strip(),

            capacity=request.POST.get(
                "capacity",
                1
            ),

            driver_name=request.POST.get(
                "driver_name",
                ""
            ).strip(),

            driver_phone=request.POST.get(
                "driver_phone",
                ""
            ).strip(),

            is_available=(
                request.POST.get(
                    "is_available"
                ) == "on"
            ),
        )

        messages.success(
            request,
            "Vehicle added successfully."
        )

        return redirect("erp_vehicles")

    return render(
        request,
        "travel_erp/vehicle_form.html"
    )


def edit_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    if request.method == "POST":

        vehicle.vehicle_number = request.POST.get(
            "vehicle_number",
            ""
        ).strip()

        vehicle.vehicle_type = request.POST.get(
            "vehicle_type"
        )

        vehicle.model = request.POST.get(
            "model",
            ""
        ).strip()

        vehicle.capacity = request.POST.get(
            "capacity",
            1
        )

        vehicle.driver_name = request.POST.get(
            "driver_name",
            ""
        ).strip()

        vehicle.driver_phone = request.POST.get(
            "driver_phone",
            ""
        ).strip()

        vehicle.is_available = (
            request.POST.get(
                "is_available"
            ) == "on"
        )

        vehicle.save()

        messages.success(
            request,
            "Vehicle updated successfully."
        )

        return redirect("erp_vehicles")

    return render(
        request,
        "travel_erp/vehicle_form.html",
        {
            "vehicle": vehicle
        }
    )


def delete_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    vehicle.delete()

    messages.success(
        request,
        "Vehicle deleted successfully."
    )

    return redirect("erp_vehicles")


def toggle_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    vehicle.is_available = not vehicle.is_available

    vehicle.save()

    return redirect("erp_vehicles")


# ============================================================
# PAYMENTS
# ============================================================

def payments(request):

    payment_list = Payment.objects.select_related(
        "booking",
        "booking__customer"
    ).order_by("-id")

    total_payments = (
        payment_list.aggregate(
            total=Sum("amount")
        )["total"]
        or Decimal("0")
    )

    return render(
        request,
        "travel_erp/payments.html",
        {
            "payments": payment_list,
            "total_payments": total_payments,
        }
    )


def add_payment(request):

    bookings_list = Booking.objects.select_related(
        "customer",
        "package"
    ).order_by("-id")

    if request.method == "POST":

        booking_id = request.POST.get(
            "booking"
        )

        amount = Decimal(
            request.POST.get(
                "amount",
                "0"
            ) or "0"
        )

        payment = Payment.objects.create(

            booking_id=booking_id,

            amount=amount,

            payment_method=request.POST.get(
                "payment_method"
            ),

            reference_number=request.POST.get(
                "reference_number",
                ""
            ).strip(),

            notes=request.POST.get(
                "notes",
                ""
            ).strip(),
        )

        booking = payment.booking

        booking.advance_amount += amount

        booking.balance_amount = (
            booking.total_amount
            - booking.advance_amount
        )

        if booking.balance_amount <= 0:

            booking.payment_status = "Paid"

        elif booking.advance_amount > 0:

            booking.payment_status = "Partial"

        else:

            booking.payment_status = "Pending"

        booking.save()

        messages.success(
            request,
            "Payment added successfully."
        )

        return redirect("erp_payments")

    return render(
        request,
        "travel_erp/payment_form.html",
        {
            "bookings": bookings_list
        }
    )


def delete_payment(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id
    )

    booking = payment.booking

    amount = payment.amount

    payment.delete()

    booking.advance_amount = max(
        Decimal("0"),
        booking.advance_amount - amount
    )

    booking.balance_amount = (
        booking.total_amount
        - booking.advance_amount
    )

    if booking.balance_amount <= 0:

        booking.payment_status = "Paid"

    elif booking.advance_amount > 0:

        booking.payment_status = "Partial"

    else:

        booking.payment_status = "Pending"

    booking.save()

    messages.success(
        request,
        "Payment deleted successfully."
    )

    return redirect("erp_payments")


# ============================================================
# EXPENSES
# ============================================================

def expenses(request):

    expense_list = Expense.objects.order_by(
        "-expense_date",
        "-id"
    )

    total_expenses = (
        expense_list.aggregate(
            total=Sum("amount")
        )["total"]
        or Decimal("0")
    )

    return render(
        request,
        "travel_erp/expenses.html",
        {
            "expenses": expense_list,
            "total_expenses": total_expenses,
        }
    )


def add_expense(request):

    if request.method == "POST":

        Expense.objects.create(

            title=request.POST.get(
                "title",
                ""
            ).strip(),

            category=request.POST.get(
                "category"
            ),

            amount=request.POST.get(
                "amount",
                0
            ),

            expense_date=request.POST.get(
                "expense_date"
            ),

            description=request.POST.get(
                "description",
                ""
            ).strip(),
        )

        messages.success(
            request,
            "Expense added successfully."
        )

        return redirect("erp_expenses")

    return render(
        request,
        "travel_erp/expense_form.html"
    )


def edit_expense(request, expense_id):

    expense = get_object_or_404(
        Expense,
        id=expense_id
    )

    if request.method == "POST":

        expense.title = request.POST.get(
            "title",
            ""
        ).strip()

        expense.category = request.POST.get(
            "category"
        )

        expense.amount = request.POST.get(
            "amount",
            0
        )

        expense.expense_date = request.POST.get(
            "expense_date"
        )

        expense.description = request.POST.get(
            "description",
            ""
        ).strip()

        expense.save()

        messages.success(
            request,
            "Expense updated successfully."
        )

        return redirect("erp_expenses")

    return render(
        request,
        "travel_erp/expense_form.html",
        {
            "expense": expense
        }
    )


def delete_expense(request, expense_id):

    expense = get_object_or_404(
        Expense,
        id=expense_id
    )

    expense.delete()

    messages.success(
        request,
        "Expense deleted successfully."
    )

    return redirect("erp_expenses")
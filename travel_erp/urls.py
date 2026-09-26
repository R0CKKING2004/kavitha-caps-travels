from django.urls import path
from . import views


urlpatterns = [

    # ==================================================
    # DASHBOARD
    # ==================================================

    path(
        "",
        views.dashboard,
        name="erp_dashboard"
    ),


    # ==================================================
    # CUSTOMERS
    # ==================================================

    path(
        "customers/",
        views.customers,
        name="erp_customers"
    ),

    path(
        "customers/add/",
        views.add_customer,
        name="add_customer"
    ),

    path(
        "customers/edit/<int:customer_id>/",
        views.edit_customer,
        name="edit_customer"
    ),

    path(
        "customers/delete/<int:customer_id>/",
        views.delete_customer,
        name="delete_customer"
    ),


    # ==================================================
    # PACKAGES
    # ==================================================

    path(
        "packages/",
        views.packages,
        name="erp_packages"
    ),

    path(
        "packages/add/",
        views.add_package,
        name="add_package"
    ),

    path(
        "packages/edit/<int:package_id>/",
        views.edit_package,
        name="edit_package"
    ),

    path(
        "packages/delete/<int:package_id>/",
        views.delete_package,
        name="delete_package"
    ),

    path(
        "packages/toggle/<int:package_id>/",
        views.toggle_package,
        name="toggle_package"
    ),


    # ==================================================
    # BOOKINGS
    # ==================================================

    path(
        "bookings/",
        views.bookings,
        name="erp_bookings"
    ),

    path(
        "bookings/add/",
        views.add_booking,
        name="add_booking"
    ),

    path(
        "bookings/edit/<int:booking_id>/",
        views.edit_booking,
        name="edit_booking"
    ),

    path(
        "bookings/delete/<int:booking_id>/",
        views.delete_booking,
        name="delete_booking"
    ),


    # ==================================================
    # VEHICLES
    # ==================================================

    path(
        "vehicles/",
        views.vehicles,
        name="erp_vehicles"
    ),

    path(
        "vehicles/add/",
        views.add_vehicle,
        name="add_vehicle"
    ),

    path(
        "vehicles/edit/<int:vehicle_id>/",
        views.edit_vehicle,
        name="edit_vehicle"
    ),

    path(
        "vehicles/delete/<int:vehicle_id>/",
        views.delete_vehicle,
        name="delete_vehicle"
    ),

    path(
        "vehicles/toggle/<int:vehicle_id>/",
        views.toggle_vehicle,
        name="toggle_vehicle"
    ),


    # ==================================================
    # PAYMENTS
    # ==================================================

    path(
        "payments/",
        views.payments,
        name="erp_payments"
    ),

    path(
        "payments/add/",
        views.add_payment,
        name="add_payment"
    ),

    path(
        "payments/delete/<int:payment_id>/",
        views.delete_payment,
        name="delete_payment"
    ),


    # ==================================================
    # EXPENSES
    # ==================================================

    path(
        "expenses/",
        views.expenses,
        name="erp_expenses"
    ),

    path(
        "expenses/add/",
        views.add_expense,
        name="add_expense"
    ),

    path(
        "expenses/edit/<int:expense_id>/",
        views.edit_expense,
        name="edit_expense"
    ),

    path(
        "expenses/delete/<int:expense_id>/",
        views.delete_expense,
        name="delete_expense"
    ),
]
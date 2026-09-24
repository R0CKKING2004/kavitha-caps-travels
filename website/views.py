from urllib.parse import quote

from django.shortcuts import render

from .forms import EnquiryForm
from packages.models import Package


def home(request):

    whatsapp_url = None
    enquiry_success = False

    if request.method == 'POST':

        form = EnquiryForm(request.POST)

        if form.is_valid():

            # Save enquiry to database
            enquiry = form.save()

            # Kavitha CAPS Travels WhatsApp number
            whatsapp_number = "919360241362"

            # WhatsApp message
            whatsapp_message = (
                "New Travel Enquiry - Kavitha CAPS Travels\n\n"
                f"Name: {enquiry.name}\n"
                f"Phone: {enquiry.phone}\n"
                f"Email: {enquiry.email or 'Not provided'}\n"
                f"Destination: {enquiry.destination}\n"
                f"Travel Date: {enquiry.travel_date}\n"
                f"Travellers: {enquiry.travellers}\n"
                f"Vehicle: {enquiry.vehicle}\n"
                f"Message: {enquiry.message or 'No additional message'}"
            )

            # Create WhatsApp click-to-chat URL
            whatsapp_url = (
                f"https://wa.me/{whatsapp_number}"
                f"?text={quote(whatsapp_message)}"
            )

            enquiry_success = True

            # Clear form after successful submission
            form = EnquiryForm()

    else:

        form = EnquiryForm()

    # Get active packages
    packages = Package.objects.filter(
        is_active=True
    ).order_by('name')

    return render(
        request,
        'website/home.html',
        {
            'form': form,
            'packages': packages,
            'whatsapp_url': whatsapp_url,
            'enquiry_success': enquiry_success,
        }
    )
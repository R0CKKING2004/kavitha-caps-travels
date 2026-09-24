from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import EnquiryForm
from packages.models import Package


def home(request):

    if request.method == 'POST':

        form = EnquiryForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Thank you! Your travel enquiry has been submitted successfully. Our team will contact you soon.'
            )

            return redirect('home')

    else:

        form = EnquiryForm()

    packages = Package.objects.filter(
        is_active=True
    ).order_by('name')

    return render(
        request,
        'website/home.html',
        {
            'form': form,
            'packages': packages,
        }
    )
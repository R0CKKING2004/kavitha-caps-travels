from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry

        fields = [
            'name',
            'phone',
            'email',
            'destination',
            'travel_date',
            'travellers',
            'vehicle',
            'message',
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your Name'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'placeholder': '10-digit Phone Number',
                    'maxlength': '10',
                    'inputmode': 'numeric'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email Address'
                }
            ),

            'destination': forms.TextInput(
                attrs={
                    'placeholder': 'Where do you want to go?'
                }
            ),

            'travel_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'travellers': forms.NumberInput(
                attrs={
                    'placeholder': 'Number of Travellers',
                    'min': '1'
                }
            ),

            'vehicle': forms.Select(),

            'message': forms.Textarea(
                attrs={
                    'placeholder':
                        'Tell us about your travel requirements',
                    'rows': 5
                }
            ),
        }


    def clean_phone(self):

        phone = self.cleaned_data.get('phone', '').strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only numbers.'
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                'Please enter a valid 10-digit phone number.'
            )

        if phone[0] not in '6789':
            raise forms.ValidationError(
                'Please enter a valid Indian mobile number.'
            )

        return phone


    def clean_travellers(self):

        travellers = self.cleaned_data.get('travellers')

        if travellers is None or travellers < 1:
            raise forms.ValidationError(
                'Number of travellers must be at least 1.'
            )

        return travellers
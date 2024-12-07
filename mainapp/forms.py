# booking/forms.py

from django import forms
from .models import Booking

# Form for making a booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_date', 'end_date']

# Form for admin to update booking status
class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']

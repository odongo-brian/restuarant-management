# booking/forms.py

from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


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

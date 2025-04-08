from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Booking 


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_type', 'pay_now', 'checkin_date', 'checkout_date', 'guests']



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

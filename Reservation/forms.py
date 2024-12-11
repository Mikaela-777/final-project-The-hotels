from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'room', 'check_in_date', 'check_out_date', 'status']

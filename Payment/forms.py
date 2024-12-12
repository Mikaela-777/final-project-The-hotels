from django import forms
from .models import Payment
from Reservation.models import Reservation

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_date', 'payment_method', 'status', 'proof_of_payment']

    # No need to pass reservation in init anymore
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

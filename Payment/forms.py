from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['reservation', 'amount', 'payment_date', 'payment_method', 'status', 'proof_of_payment']

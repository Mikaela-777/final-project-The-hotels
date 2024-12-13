from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_date', 'payment_method', 'status', 'proof_of_payment']
        widgets = {
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'proof_of_payment': forms.FileInput(attrs={'class': 'form-control'}),
        }


    # No need to pass reservation in init anymore
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Reservation
from .forms import PaymentForm

# Create Payment
def create_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    reservations = Reservation.objects.all()  # Untuk dropdown reservasi
    return render(request, 'payments/create.html', {'form': form, 'reservations': reservations})

# Delete Payment
def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        payment.delete()
        return redirect('payment_list')
    return render(request, 'payments/delete.html', {'payment': payment})

# Payment List
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payments/list.html', {'payments': payments})

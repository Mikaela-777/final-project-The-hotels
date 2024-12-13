from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from Reservation.models import Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def create_payment(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)

    # Jika metode request adalah POST, proses pembayaran
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            # Tentukan jumlah pembayaran sesuai harga kamar
            payment = form.save(commit=False)
            payment.reservation = reservation
            payment.amount = reservation.room.price_per_night  # Set jumlah pembayaran sesuai harga kamar
            payment.status = 'completed'  # Status pembayaran di-set ke 'completed'
            payment.save()

            # Setelah pembayaran selesai, baru ubah status reservasi menjadi 'completed' dan 'payed'
            reservation.payment_status = 'payed'
            reservation.status = 'completed'
            reservation.save()

            messages.success(request, 'Pembayaran berhasil.')
            return redirect('payment_list')  # Arahkan ke daftar pembayaran setelah berhasil
    else:
        form = PaymentForm()

    context = {
        'form': form,
        'reservation': reservation
    }

    return render(request, 'payments/create.html', context)

# Payment List
@login_required
def payment_list(request):
    payments = Payment.objects.filter(reservation__user=request.user)
    return render(request, 'payments/list.html', {'payments': payments})

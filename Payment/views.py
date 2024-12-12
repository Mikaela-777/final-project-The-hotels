from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from .models import Payment
from Reservation.models import Reservation
from django.contrib import messages

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

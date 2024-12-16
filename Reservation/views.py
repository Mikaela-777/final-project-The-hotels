from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm, ReservationListForm, CancelReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create
@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.status = 'booked'
            reservation.payment_status = form.cleaned_data['payment_status']  # Set status pembayaran
            reservation.save()
            messages.success(request, 'Reservasi berhasil dibuat!')
            return redirect('reservation_list')
        else:
            messages.error(request, 'Ruang ini sudah dipesan pada tanggal ini.')
    else:
        form = ReservationForm()
    
    return render(request, 'reservations/create.html', {'form': form})

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-check_in')
    return render(request, 'reservations/list.html', {'reservations': reservations})

def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        reservation.status = 'cancelled'
        reservation.payment_status = 'canceled'
        reservation.save()
        messages.success(request, 'Reservasi berhasil dibatalkan.')
        return redirect('reservation_list')  # Redirect ke daftar reservasi

    # Jika tidak memerlukan konfirmasi, bisa langsung handle POST di daftar reservasi
    return redirect('reservation_list')

@login_required
def reservation_list_hotel(request):
    form = ReservationListForm(request.GET or None)
    reservations = Reservation.objects.all()

    if form.is_valid():
        # Ambil data dari form
        user = form.cleaned_data.get('user')  # Username (string) dari form
        room = form.cleaned_data.get('room')
        status = form.cleaned_data.get('status')

        # Terapkan filter berdasarkan input pengguna
        if user:
            reservations = reservations.filter(user__username__icontains=user)
        if room:
            reservations = reservations.filter(room__room_number__icontains=room)
        if status:
            reservations = reservations.filter(status=status)

    context = {
        'form': form,
        'reservations': reservations,
    }
    return render(request, 'reservations/hotel_list.html', context)
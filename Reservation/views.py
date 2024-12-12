from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm, ReservationListForm
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
            messages.error(request, 'Terjadi kesalahan dalam pembuatan reservasi.')
    else:
        form = ReservationForm()

    return render(request, 'reservations/create.html', {'form': form})

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-check_in')
    return render(request, 'reservations/list.html', {'reservations': reservations})

# Delete
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/delete.html', {'reservation': reservation})

def confirm_payment(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.confirm_reservation()
    return redirect('reservation_detail', reservation_id=reservation.id)

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.cancel_reservation()
    return redirect('reservation_detail', reservation_id=reservation.id)

@login_required
def reservation_list_hotel(request):
    form = ReservationListForm(request.GET or None)
    reservations = Reservation.objects.filter(user=request.user)  # Hanya milik user login
    
    if form.is_valid():
        room = form.cleaned_data.get('room')
        status = form.cleaned_data.get('status')

        if room:
            reservations = reservations.filter(room__room_number__icontains=room)
        if status:
            reservations = reservations.filter(status=status)
    
    context = {
        'form': form,
        'reservations': reservations,
    }
    return render(request, 'reservations/hotel_list.html', context)

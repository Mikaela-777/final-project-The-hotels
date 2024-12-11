from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm

# Create
def create_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')  # Redirect ke halaman daftar reservasi
    else:
        form = ReservationForm()
    return render(request, 'reservations/create.html', {'form': form})

# Delete
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/delete.html', {'reservation': reservation})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/list.html', {'reservations': reservations})

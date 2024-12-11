from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

# Create
@login_required
def create_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Tetapkan user yang sedang login sebagai pemesan
            reservation.save()
            return redirect('reservation_list')
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
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/list.html', {'reservations': reservations})

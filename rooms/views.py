from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from .forms import RoomForm
from django.db.models import Count, Q
from django.utils import timezone

# Create
def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # Redirect ke halaman daftar Room
    else:
        form = RoomForm()
    return render(request, 'rooms/create.html', {'form': form})

# Edit
# Edit Room View
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('setting_room')
    else:
        form = RoomForm(instance=room)
        
    return render(request, 'rooms/edit.html', {'form': form, 'room': room})


# Delete Room View
def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'rooms/delete.html', {'room': room})

def room_list(request):
    today = timezone.now().date()  # Get today's date

    # Count available rooms by excluding rooms with overlapping bookings for today
    single_rooms = Room.objects.filter(room_type='Single').annotate(
        booked_count=Count('reservation', filter=Q(reservation__status='booked') &
                                             Q(reservation__check_in__lte=today) &
                                             Q(reservation__check_out__gte=today))
    )

    double_rooms = Room.objects.filter(room_type='Double').annotate(
        booked_count=Count('reservation', filter=Q(reservation__status='booked') &
                                             Q(reservation__check_in__lte=today) &
                                             Q(reservation__check_out__gte=today))
    )

    suite_rooms = Room.objects.filter(room_type='Suite').annotate(
        booked_count=Count('reservation', filter=Q(reservation__status='booked') &
                                             Q(reservation__check_in__lte=today) &
                                             Q(reservation__check_out__gte=today))
    )

    # Calculate the number of available rooms (total rooms - booked rooms for today)
    context = {
        'single_rooms_count': single_rooms.count() - single_rooms.filter(booked_count__gt=0).count(),
        'double_rooms_count': double_rooms.count() - double_rooms.filter(booked_count__gt=0).count(),
        'suite_rooms_count': suite_rooms.count() - suite_rooms.filter(booked_count__gt=0).count(),
        'single_room_price': single_rooms.first().price_per_night if single_rooms.exists() else 0,
        'double_room_price': double_rooms.first().price_per_night if double_rooms.exists() else 0,
        'suite_room_price': suite_rooms.first().price_per_night if suite_rooms.exists() else 0,
    }

    return render(request, 'rooms/list.html', context)

def pesan_kamar(request, room_type):
    # Logika pemesanan atau kirim pesan konfirmasi untuk jenis kamar
    return render(request, 'reservations/create.html', {'room_type': room_type})

def room_setting(request):
    rooms = Room.objects.all().order_by('room_number')
    return render(request, 'rooms/room_setting.html', {'rooms': rooms})

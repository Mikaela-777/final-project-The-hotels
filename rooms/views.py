from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

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
            return redirect('room_list')
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
    # Hitung jumlah ruangan untuk setiap tipe dan ambil harga yang relevan
    single_rooms = Room.objects.filter(room_type='Single', status=True)
    double_rooms = Room.objects.filter(room_type='Double', status=True)
    suite_rooms = Room.objects.filter(room_type='Suite', status=True)

    # Mengambil harga unik dari masing-masing tipe ruangan
    single_room_price = single_rooms.first().price_per_night if single_rooms.exists() else 0
    double_room_price = double_rooms.first().price_per_night if double_rooms.exists() else 0
    suite_room_price = suite_rooms.first().price_per_night if suite_rooms.exists() else 0

    context = {
        'single_rooms_count': single_rooms.count(),
        'double_rooms_count': double_rooms.count(),
        'suite_rooms_count': suite_rooms.count(),
        'single_room_price': single_room_price,
        'double_room_price': double_room_price,
        'suite_room_price': suite_room_price,
    }
    return render(request, 'rooms/list.html', context)

def pesan_kamar(request, room_type):
    # Logika pemesanan atau kirim pesan konfirmasi untuk jenis kamar
    return render(request, 'reservations/create.html', {'room_type': room_type})

def room_setting(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_setting.html', {'rooms': rooms})

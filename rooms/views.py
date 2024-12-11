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
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'rooms/edit.html', {'form': form, 'room': room})

# Delete
def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        room.delete()
        return redirect('room_list')
    return render(request, 'rooms/delete.html', {'room': room})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/list.html', {'rooms': rooms})

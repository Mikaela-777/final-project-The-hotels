from django import forms
from .models import Reservation, Room
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput

class ReservationForm(forms.ModelForm):
    room = forms.ModelChoiceField(
        queryset=Room.objects.all().order_by('price_per_night', 'room_number'),
        empty_label="Select a room"
    )

    class Meta:
        model = Reservation
        fields = ['room', 'check_in', 'check_out','payment_status']
        widgets = {
            'check_in': DateInput(attrs={'type': 'date'}),  # Menambahkan widget langsung di Meta
            'check_out': DateInput(attrs={'type': 'date'})  # Menambahkan widget langsung di Meta
        }

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        # Validasi jika check-in tidak boleh lebih dari check-out
        if check_in and check_out and check_in >= check_out:
            raise ValidationError("Tanggal check-in harus sebelum tanggal check-out.")

        # Memeriksa jika ada reservasi yang bentrok dengan tanggal yang dipilih dan statusnya 'booked'
        conflicting_reservations = Reservation.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in,
            payment_status='booked'  # Cek hanya reservasi yang statusnya 'booked'
        )

        if conflicting_reservations.exists():
            raise ValidationError("Ruangan ini sudah dipesan pada tanggal yang dipilih.")

        return cleaned_data


class ReservationListForm(forms.Form):
    user = forms.CharField(required=False, label="User", widget=forms.TextInput(attrs={'class': 'form-control'}))
    room = forms.CharField(required=False, label="Room", widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'All'), ('booked', 'booked'), ('cancelled', 'cancelled'), ('completed', 'completed')],
        label="Status",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class CancelReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = []  # Tidak ada input karena pembatalan otomatis mengatur status

    def save(self, commit=True):
        reservation = super().save(commit=False)
        reservation.status = 'cancelled'  # Ubah status menjadi 'cancelled'
        reservation.payment_status = 'canceled'  # Ubah payment_status menjadi 'canceled'
        if commit:
            reservation.save()
        return reservation
from django.db import models
from rooms.models import Room
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Dipesan'),
        ('cancelled', 'Dibatalkan'),
        ('completed', 'Selesai'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('payed', 'Payed'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')  # New field

    def clean(self):
        if self.status != 'completed':  # Cek hanya jika statusnya bukan 'completed'
            conflicting_reservations = Reservation.objects.filter(
                room=self.room,
                check_in__lt=self.check_out,
                check_out__gt=self.check_in,
                status='booked'  # Periksa hanya reservasi dengan status 'booked'
            )

            if conflicting_reservations.exists():
                raise ValidationError(_('Ruangan ini sudah dipesan untuk tanggal tersebut.'))

        return super().clean()


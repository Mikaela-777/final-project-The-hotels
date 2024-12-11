from django.db import models
from rooms.models import Room

# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed')

    def __str__(self):
        return f"Reservation for {self.guest.name} in {self.room.room_type}"

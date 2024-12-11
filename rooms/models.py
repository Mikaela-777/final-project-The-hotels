from django.db import models

# Create your models here.
class Room(models.Model):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    SUITE = 'Suite'
    ROOM_TYPES = [
        (SINGLE, 'Single'),
        (DOUBLE, 'Double'),
        (SUITE, 'Suite'),
    ]
    
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Room {self.room_number}: {self.room_type} - ${self.price_per_night}/night"

from django.db import models
from Reservation.models import Reservation
from django.utils.timezone import now
# Create your models here.
class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=now)
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('cash', 'Cash'),
            ('Gopay', 'Gopay'),
            ('QRIS', 'QRIS'),
            ('Dana', 'Dana'),
        ]
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('completed', 'Completed'),
            ('refunded', 'Refunded'),
        ]
        ,default='completed'
    )
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    proof_of_payment = models.ImageField(upload_to='static/images/payment_proofs/', blank=True, null=True)

    def __str__(self):
        return f"Payment {self.id} - {self.amount} ({self.get_status_display()})"
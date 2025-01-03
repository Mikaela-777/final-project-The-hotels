# Generated by Django 5.1.3 on 2024-12-10 13:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('cash', 'Cash'), ('bank_transfer', 'Bank Transfer'), ('e_wallet', 'E-Wallet')], max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('refunded', 'Refunded')], max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('proof_of_payment', models.ImageField(blank=True, null=True, upload_to='payment_proofs/')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.reservation')),
            ],
        ),
    ]

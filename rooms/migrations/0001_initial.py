# Generated by Django 5.1.3 on 2024-12-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('room_type', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite')], max_length=10)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
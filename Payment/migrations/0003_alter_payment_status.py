# Generated by Django 5.1.3 on 2024-12-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_alter_payment_payment_method_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(default='completed', max_length=20),
        ),
    ]

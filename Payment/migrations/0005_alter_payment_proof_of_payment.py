# Generated by Django 5.1.3 on 2024-12-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0004_alter_payment_payment_method_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='proof_of_payment',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/payment_proofs/'),
        ),
    ]

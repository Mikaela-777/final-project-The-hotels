# Generated by Django 5.1.3 on 2024-12-12 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_utama', '0002_alter_userprofile_address_alter_userprofile_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='anonim', max_length=100),
        ),
    ]

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    # Tambahkan field lain sesuai kebutuhan
    name = models.CharField(max_length=100,default="anonim")
    phone_number = models.CharField(max_length=12,null=True)
    address = models.CharField(max_length=50,null=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
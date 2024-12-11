from django.db import models

class Order(models.Model):
    # Tambahkan field sesuai kebutuhan
    customer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    # Tambahkan field lain sesuai kebutuhan
    name = models.CharField(max_length=100,default="tai nando")
    phone_number = models.CharField(max_length=12,null=True)
    address = models.CharField(max_length=50,null=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
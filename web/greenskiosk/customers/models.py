from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Customer(models.Model):
    GENDERS = (
        ("m", "male"),
        ("f", "female")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDERS)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    email = models.EmailField()

class Shipping_Addresss(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    notes = models.TextField()

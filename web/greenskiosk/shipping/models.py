from django.db import models

from catalogue.models import Product

# Create your models here.


class Shipping_Provider(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    transport_mode = models.CharField(max_length=30)

class Dispenser_cooler_box(models.Model):
    box_number = models.IntegerField()
    location = models.CharField(max_length=30)
    unlock_code = models.IntegerField()

class Product_Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

from django.db import models

from kiosks.models import Kiosk


# Create yoobjects.createur models here.
from django.contrib.auth.models import User


class Product_supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    street_address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    id_number = models.IntegerField()
    date_added = models.DateField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.email
    


class Product_Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    icon = models.ImageField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=10)
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    supplier_price = models.DecimalField(max_digits=20, decimal_places=10)
    selling_price = models.DecimalField(max_digits=20, decimal_places=10)
    supplier = models.ForeignKey(Product_supplier, on_delete=models.CASCADE)
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE)
    number_in_stock = models.ImageField()

    def __str__(self):
        return self.title
    


class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()


from django.db import models

from catalogue.models import Product
from customers.models import Customer


# Create your models here.

class Cart(models.Model):
   products = models.ManyToManyField(Product)
   date_created = models.DateField()
#    total_price = models.DecimalField(max_digits=20, decimal_places=10)
   status = models.CharField(max_length=30)
   

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=30)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    date_of_payment = models.DateTimeField()


class Order(models.Model):
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=30)
    # basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    # shipping_provider = models.ForeignKey(Shipping_provider, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=20, decimal_places=10)
    shipping_cost = models.DecimalField(max_digits=20, decimal_places=10)
    total_price = models.DecimalField(max_digits=20, decimal_places=10)
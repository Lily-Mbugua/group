from django.contrib import admin

# Register your models here.

from .models import Customer, Shipping_Addresss

admin.site.register(Shipping_Addresss)
admin.site.register(Customer)
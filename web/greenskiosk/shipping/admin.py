from django.contrib import admin

# Register your models here.

from .models import Dispenser_cooler_box, Shipping_Provider, Product_Review

admin.site.register(Product_Review)
admin.site.register(Shipping_Provider)
admin.site.register(Dispenser_cooler_box)
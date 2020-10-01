from django.contrib import admin

# Register your models here.


from .models import Product_supplier, Product_Image, Product_Category, Product

admin.site.register(Product)
admin.site.register(Product_Category)
admin.site.register(Product_Image)
admin.site.register(Product_supplier)


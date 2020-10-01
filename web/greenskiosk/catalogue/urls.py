from django.urls import path
from .views import products_list, products_details
from . import views

urlpatterns = [
    path('products/', products_list, name='products-list'),
    path('details/', products_details, name='products_details')
]
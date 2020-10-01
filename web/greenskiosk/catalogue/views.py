from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def products_details(request):
    return render(request, 'products_details.html')
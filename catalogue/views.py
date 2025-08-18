from django.shortcuts import render

# Create your views here.
from .models import Product


def list_products(request):
    products = Product.objects.all()
    
    return render(request, 'catalogue/products.html', {'products':products})

# requests, destination, catalogue

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "catalogue/product_details.html", {"product": product})
from django.shortcuts import render
from .models import Product

def product_list(request):
    # Pega todos os produtos disponíveis no banco de dados
    products = Product.objects.filter(is_available=True)
    
    # Envia os produtos para uma página HTML (template)
    return render(request, 'products/product_list.html', {'products': products})

def home(request):
    # Pega os 3 primeiros produtos disponíveis para colocar em destaque
    featured_products = Product.objects.filter(is_available=True)[:3]
    return render(request, 'products/home.html', {'featured_products': featured_products})
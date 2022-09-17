from itertools import product
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Create your views here.   
def all_products(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def categories(request):
    return{
        'categories': Category.objects.filter(parent=None)
    }

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.all()
    return render(request, 'category_list.html', {'products': products, 'category': category})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})



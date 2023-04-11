from django.shortcuts import render,redirect
from .forms import CategoryForm, ProductForm
from .models import Category, Product
# Create your views here.





def men_product(request):
    return render(request, 'product/men-product.html')


def women_product(request):
    return render(request, 'product/women-product.html')


def kid_product(request):
    return render(request, 'product/kid-product.html')
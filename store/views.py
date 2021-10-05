from django.shortcuts import render
from .models import Category,Product
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return  render(request,'store/home.html',context={
        'products':products,
        'categories':categories,
    })



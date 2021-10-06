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


def category_products(request,category_id):
    products = Product.objects.filter(category__id = category_id)
    categories = Category.objects.all()
    return render(request,'store/home.html',context={
        "products":products,
        'categories':categories,
    })
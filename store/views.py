from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
# Create your views here.

def all_products(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    p = Paginator(products, 3)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    return  render(request,'store/home.html',context={
        'list_products':products_list,
        'categories':categories,
    })


def category_products(request,category_id):
    products = Product.objects.filter(category__id = category_id,is_active=True)
    categories = Category.objects.all()
    p = Paginator(products, 3)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    return render(request,'store/home.html',context={
        "list_products":products_list,
        'categories':categories,
    })

def product_detail(request,product_id):
    categories = Category.objects.all()
    product = get_object_or_404(Product,id=product_id)
    cart_product_form = CartAddProductForm()
    return render(request,'store/detail.html',context={
        "categories":categories,
        'product':product,
        'cart_product_form':cart_product_form,
    })
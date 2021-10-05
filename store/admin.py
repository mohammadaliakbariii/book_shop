from django.contrib import admin
from .models import Category,Product
# Register your models here.

@admin.register(Category)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title','author','price','is_stock','is_active','created','updated'
    ]
    list_filter = ['is_stock', 'is_active']
    list_editable = ['price',"is_stock"]


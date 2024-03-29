from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('',views.all_products,name='all_products'),
    path("category/<int:category_id>/",views.category_products,name = "category_products"),
    path('product/<int:product_id>/',views.product_detail,name='product_detail'),
]
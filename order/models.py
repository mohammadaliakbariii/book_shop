from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from store.models import Product
from accounts.models import CustomUser
from store.models import Product

class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total = models.FloatField(default=0)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_item = models.IntegerField(default=0)
    quantity =  models.IntegerField(default=1)

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from store.models import Product
from accounts.models import Customer

class Order_items(models.Model):
    products=models.ManyToManyField(Product)


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_items=models.ForeignKey(Order_items,on_delete=models.CASCADE)
    start_date=models.DateTimeField(auto_now_add=True)
    date=models.DateTimeField()
    address=models.TextField()
    ready='ready'
    not_ready='note ready'
    posted="posted"
    status_choice=(
        (ready,"ready"),
        (not_ready,"not ready"),
        (posted,"posted")
    )
    status=models.CharField(max_length=20,choices=status_choice,default=not_ready)
    def __str__(self):
        return f"order of {self.customer.email}"



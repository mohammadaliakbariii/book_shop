from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,related_name="product",on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='product_creator',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100,default='admin')
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    is_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title

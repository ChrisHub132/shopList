from itertools import product
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model): 
    catName = models.CharField(max_length=40)
    

    class Meta:
        verbose_name_plural = 'Produkt-Gruppen'

    def __str__(self):
        return self.catName



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    prodName = models.CharField(max_length=255)
    ## image = models.ImageField(upload_to='item_images', blank=True, null=True)


    def __str__(self):
        return self.prodName

    class Meta:
        ordering = ['id']

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cartProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.cartProduct}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")


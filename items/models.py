from django.db import models

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

from django.db import models
from random import *

product_image=()
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100,verbose_name='Category',blank=True,null=True)
    
    def __str__(self):
        return self.category_name

class Available(models.Model):
    website_name=models.CharField(max_length=100,verbose_name='Name of Website',blank=True,null=True)
    product_price=models.FloatField(default=100,verbose_name='Product Price Rs')
    shiping_charge=models.FloatField(default=1,verbose_name='shipping charge')
    stock=models.PositiveIntegerField(default=1,verbose_name='Quantity of Product')

class Seller(models.Model):
    seller_id=models.IntegerField(verbose_name='Seller ID')
    name=models.CharField(max_length=100,verbose_name='Seller Name',blank=True,null=True)
    city=models.CharField(max_length=100,verbose_name='City',blank=True,null=True)

class Product(models.Model):
    product_id=models.IntegerField(default=1,verbose_name='Product_ID')
    prod_ID=randint(product_id)
    product_name=models.CharField(max_length=100,verbose_name='Product Name',blank=True,null=True)
    company_name=models.CharField(max_length=100,verbose_name='Comapny Name',blank=True,null=True)
    product_price=models.FloatField(default=100,verbose_anme='Avrage Product Price')
    gst=models.FloatField(default=1,verbose_name='GST')
    seller=models.OneToOneField(Seller,verbose_name='Seller Address')
    available_on=models.ManyToManyField(Available,verbose_name='Product available on',on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id



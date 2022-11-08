from rest_framework.serializers import ModelSerializer
from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['prod_ID','product_name','company_name','product_price','seller','available_on']

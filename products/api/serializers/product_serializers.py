from products.models import Product
from rest_framework import serializers

class ProductSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ['state',]

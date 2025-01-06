from rest_framework import serializers
from minha_lanchonete.models.Product import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ("id", "name", "value")
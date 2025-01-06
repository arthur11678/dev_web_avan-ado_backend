from rest_framework import serializers
from minha_lanchonete.models.Product import Product

class ProductSerializer(serializers.Serializer):
    
    class Meta:
        model = Product
        fields = ("id", "name", "value")
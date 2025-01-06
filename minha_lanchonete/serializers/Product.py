from rest_framework import serializers
from models.Product import Product

class ProductSerializer(serializers.Serializer):
    
    class Meta:
        model = Product
        fields = ("id", "name", "value")
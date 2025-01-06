from rest_framework import serializers
from models.Pizza import Pizza


class PizzaSerializer(serializers.Serializer):
    
    class Meta:
        model = Pizza
        fields = ("id", "name", "value", "size", "description")
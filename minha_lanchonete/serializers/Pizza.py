from rest_framework import serializers
from minha_lanchonete.models.Pizza import Pizza


class PizzaSerializer(serializers.Serializer):
    
    class Meta:
        model = Pizza
        fields = ("id", "name", "value", "size", "description")
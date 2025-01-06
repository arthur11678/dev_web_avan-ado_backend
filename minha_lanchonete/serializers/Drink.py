from rest_framework import serializers
from minha_lanchonete.models import Drink

class DrinkSerializer(serializers.Serializer):
    
    class Meta:
        model = Drink
        fields = ("id", "name", "value", "valume", "type")
from rest_framework import serializers
from models import Drink

class DrinkSerializer(serializers.Serializer):
    
    class Meta:
        model = Drink
        fields = ("id", "name", "value", "valume", "type")
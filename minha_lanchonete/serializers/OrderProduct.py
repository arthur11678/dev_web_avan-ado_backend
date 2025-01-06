from rest_framework import serializers
from models.OrderProduct import OrderProduct
from serializers.Order import OrderSerializer
from serializers.Product import ProductSerializer

class OrderProductSerializer(serializers.Serializer):
    
    id_order = OrderSerializer(many=False)
    id_product = ProductSerializer(many=False)
    
    class Meta:
        model = OrderProduct
        fields = ("id", "id_order", "id_product")
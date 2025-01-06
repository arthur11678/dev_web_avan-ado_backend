from rest_framework import serializers
from minha_lanchonete.models import Order, OrderProduct
from minha_lanchonete.serializers.PaymentMethod import PaymentMethodSerializer
from minha_lanchonete.helpers import ProductHelper

from users.serializers import ClientSerializer

class OrderSerializer(serializers.Serializer):
    
    client = ClientSerializer(many=False)
    payment_method = PaymentMethodSerializer(many=False)
    
    class Meta:
        model = Order
        fields = ("id", "ordered_at", "client", "payment_method")
        
class OrderWithProductsSerializer(serializers.Serializer):
    
    client = ClientSerializer(many=False)
    payment_method = PaymentMethodSerializer(many=False)
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ("id", "ordered_at", "client", "id_payment_method", "products")
        
    def get_products(self, obj):
        order_products = OrderProduct.objects.filter(id_order=obj.id)
        field = []
        for order_product in order_products:
            if(ProductHelper.is_drink(order_product.product)):    
                field.append({
                    "id": order_product.product.id,
                    "name": order_product.product.name,
                    "value": order_product.product.value,
                    "volume": order_product.product.drink.volume,
                    "type": order_product.product.drink.type
                })
            if(ProductHelper.is_pizza(order_product.product)):
                field.append({
                    "id": order_product.product.id,
                    "name": order_product.product.name,
                    "value": order_product.product.value,
                    "size": order_product.product.pizza.size,
                    "description": order_product.product.pizza.description
                })
from rest_framework import serializers
from minha_lanchonete.models import Order, OrderProduct
from users.serializers.UserSerializer import ClientSerializer
from minha_lanchonete.serializers.PaymentMethod import PaymentMethodSerializer

class OrderSerializer(serializers.Serializer):
    
    id_client = ClientSerializer(many=False)
    id_payment_method = PaymentMethodSerializer(many=False)
    
    class Meta:
        model = Order
        fields = ("id", "ordered_at", "id_client", "id_payment_method")
        
class OrderWithProductsSerializer(serializers.Serializer):
    
    id_client = ClientSerializer(many=False)
    id_payment_method = PaymentMethodSerializer(many=False)
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ("id", "ordered_at", "id_client", "id_payment_method", "products")
        
    def get_products(self, obj):
        order_products = OrderProduct.objects.filter(id_order=obj.id)
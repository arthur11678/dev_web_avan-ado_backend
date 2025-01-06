from rest_framework import serializers
from models.PaymentMethod import PaymentMethod
from users.serializers.UserSerializer import ClientSerializer

class PaymentMethodSerializer(serializers.Serializer):
    
    id_client = ClientSerializer(many=False)
    
    class Meta:
        model = PaymentMethod
        fields = ("id", "number", "id_client")
from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "name", "phone", "email")

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "name", "phone", "email", "pis_pasep", "admission_at")
        
class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "name", "phone", "email", "cpf", "address")
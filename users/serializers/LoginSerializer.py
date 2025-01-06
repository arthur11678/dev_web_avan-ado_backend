from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from users.serializers.UserSerializer import AdminSerializer, ClientSerializer

from users.helpers import UserHelper

class LoginSerializer(TokenObtainPairSerializer):
    
    @classmethod 
    def get_token(cls, user):
        return super().get_token(user)
    
    
    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.get(email=self.user)
        serializer = None
        if UserHelper.is_admin(user):
            serializer = AdminSerializer(user)
        else:
            serializer = ClientSerializer(user)
        data["user"] = serializer.data
        return data
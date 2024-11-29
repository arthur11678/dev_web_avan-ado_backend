from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response

from users.models import Admin, User
from users.serializers import UserSerializer, AdminSerializer
from users.helpers import UserHelper


class AdminsView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (permissions.IsAuthenticated)
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def create(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
        user = User.objects.create(name=name, phone=phone, email=email)
        user.set_password(request.data['password'])
        pis_pasep = request.data['pis_pasep']
        admission_at = request.data['admission_at']
        admin = Admin.objects.create(user=user, pis_pasep=pis_pasep, admission_at=admission_at)
        return Response(status=204)

    def retrieve(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        instance = self.get_object()
        return Response(data=AdminSerializer(instance, many=False).data)
    
    def list(self, request, *args, **kwargs): 
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)  
        admins = User.objects.filter()
        return super().list(request, *args, **kwargs)
    
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import PaymentMethod
from minha_lanchonete.serializers import PaymentMethodSerializer
from users.helpers import UserHelper

class PaymentMethodView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        if(not UserHelper.is_client(request.user)):
            return(Response(status=403))
        payment_methods = PaymentMethod.objects.filter(id_client=request.user.client.id)
        return(Response(data=PaymentMethodSerializer(payment_methods, many=True).data))
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if(UserHelper.is_client(request.user) and instance.id_client != request.user.client.id):
            return(Response(status=403))
        return super().destroy(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        if(not UserHelper.is_client(request.user)):
            return(Response(status=403))
        payment_method = PaymentMethod.objects.create(number=request.data['number'], id_client=request.user.client.id)
        return Response(data=PaymentMethodSerializer(payment_method, many=False))
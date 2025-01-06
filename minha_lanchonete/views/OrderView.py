from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import Order, OrderProduct
from minha_lanchonete.serializers import OrderSerializer


class OrderView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        orders = Order.objects.all()
        return Response(data=OrderSerializer(orders, many=True).data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data['status']
        instance.save()
        return Response(data=OrderSerializer(instance, many=False).data)
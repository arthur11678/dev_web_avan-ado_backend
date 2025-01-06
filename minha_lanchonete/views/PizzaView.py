from itertools import product
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import Pizza, Product
from minha_lanchonete.serializers import PizzaSerializer
from users.helpers import UserHelper

class PizzaView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return(Response(status=403))
        product = Product.objects.create(name=request.data['name'], picture=request.data['picture'], value=request.data['value'])
        pizza = Pizza.objects.create(id_product=product.id, size=request.data['size'], description=request.data['description'])
        return Response(data=PizzaSerializer(pizza, many=False))
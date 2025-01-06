from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from minha_lanchonete.models import Product, Drink, Pizza
from minha_lanchonete.serializers import DrinkSerializer, PizzaSerializer, ProductSerializer
from minha_lanchonete.helpers import ProductHelper
from users.helpers import UserHelper


class ProductView(viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        drinks = Drink.objects.all()
        pizzas = Pizza.objects.all()
        return Response(data={"drinks": DrinkSerializer(drinks, many=True).data, "pizzas": PizzaSerializer(pizzas, many=True).data})
    
    def destroy(self, request, *args, **kwargs):
        if(not UserHelper.is_admin(request.user)):
            return Response(status=403)
        instance = self.get_object()
        if(ProductHelper.is_drink(instance)):
            drink = Drink.objects.get(id=instance.drink.id)
            drink.delete()
            drink.save()
            return super().destroy(request, *args, **kwargs)
        elif(ProductHelper.is_pizza(instance)):
            pizza = Pizza.objects.get(id=instance.pizza.id)
            pizza.delete()
            pizza.save()
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=500)
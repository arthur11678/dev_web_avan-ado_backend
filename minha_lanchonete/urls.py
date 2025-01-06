from django.urls import path, include
from rest_framework import routers

from minha_lanchonete import views

router = routers.DefaultRouter()

router.register(r'product/drink', views.DrinkView)
router.register(r'order', views.OrderView)
router.register(r'payment_method', views.PaymentMethodView)
router.register(r'pizza', views.PizzaView)
router.register(r'product', views.ProductView)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'auth/', include("users.urls"))
]

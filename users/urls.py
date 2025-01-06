from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path, include

from users import views


urlpatterns = [
    path('sign-in/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('sign-up/', views.RegisterView.as_view(), name="auth_register")
]

from django.urls import path

from users.apps import UsersConfig
from users.views import CreateUserAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('users/register', CreateUserAPIView.as_view(), name='register_user'),

    # drf-simplejwt
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

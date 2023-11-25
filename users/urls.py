from django.urls import path

from users.apps import UsersConfig
from users.views import CreateUserAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/register', CreateUserAPIView.as_view(), name='register_user')
]

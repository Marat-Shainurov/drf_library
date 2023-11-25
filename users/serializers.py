from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    @staticmethod
    def validate_password(value: str) -> str:
        return make_password(value)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'registration_date')

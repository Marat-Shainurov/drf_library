from rest_framework import generics, status
from rest_framework.response import Response

from users.serializers import CustomUserCreateSerializer, CustomUserSerializer
from users.tasks import greet_new_user


class CreateUserAPIView(generics.CreateAPIView):
    """
    Creates a new CustomUser instance.
    Uses the CustomUserCreateSerializer serializers as the request body schema,
    and the CustomUserSerializer as the response body.
    """
    serializer_class = CustomUserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            greet_new_user.delay(username=new_user.username, user_email=new_user.email)
            response_serializer = CustomUserSerializer(serializer.instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

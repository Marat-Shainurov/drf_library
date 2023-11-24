from rest_framework import generics

from library.models import Book
from library.serializers import BookSerializer


class CreateBookAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer


class RetrieveBookAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListBooksAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateBookAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteBookAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

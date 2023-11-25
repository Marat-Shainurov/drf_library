from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from library.models import Book
from library.serializers import BookSerializer


class CreateBookAPIView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Uses BookSerializer as the request body schema.
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class RetrieveBookAPIView(generics.RetrieveAPIView):
    """
    Returns a  Book instance stored in the database by its id.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class ListBooksAPIView(generics.ListAPIView):
    """
    Returns a list of Book instances stored in the database.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UpdateBookAPIView(generics.UpdateAPIView):
    """
    Updates a Book instance in the database by its id.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class DeleteBookAPIView(generics.DestroyAPIView):
    """
    Deletes a Book instance from the database by its id.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

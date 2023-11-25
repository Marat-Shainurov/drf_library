from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from library.models import Book
from library.serializers import BookSerializer, BookCreateSerializer


class CreateBookAPIView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Uses BookSerializer as the request body schema, and BookSerializer as the response schema.
    """
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_serializer = BookSerializer(serializer.instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

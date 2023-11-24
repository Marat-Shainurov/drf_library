from django.urls import path

from library.apps import LibraryConfig
from library.views import CreateBookAPIView, RetrieveBookAPIView, ListBooksAPIView, DeleteBookAPIView, UpdateBookAPIView

app_name = LibraryConfig.name

urlpatterns = [
    path('library/books', ListBooksAPIView.as_view(), name='get_books'),
    path('library/books/create', CreateBookAPIView.as_view(), name='create_book'),
    path('library/books/get/<int:pk>', RetrieveBookAPIView.as_view(), name='get_book'),
    path('library/books/update/<int:pk>', UpdateBookAPIView.as_view(), name='update_book'),
    path('library/books/delete/<int:pk>', DeleteBookAPIView.as_view(), name='delete_book')
]

from django.urls import path
from rest_framework import generics

from book.models import Book
from book.serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    API View for a List of Books
    """
    queryset = Book.objects.prefetch_related('authors')
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    """
    API View for a single Book
    """
    queryset = Book.objects.prefetch_related('authors')
    serializer_class = BookSerializer


# API urlpatterns declared separately from views urls
urlpatterns = [
    path('', BookList.as_view(), name='api-book-list'),
    path('<int:pk>', BookDetail.as_view(), name='api-book-detail'),
]

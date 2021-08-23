from django.urls import path
from rest_framework import generics

from book.models import Book
from book.serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.prefetch_related('authors')
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.prefetch_related('authors')
    serializer_class = BookSerializer


urlpatterns = [
    path('', BookList.as_view(), name='api-book-list'),
    path('<int:pk>', BookDetail.as_view(), name='api-book-detail'),
]

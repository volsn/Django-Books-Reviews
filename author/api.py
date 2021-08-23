from rest_framework import generics

from author.models import Author
from author.serializers import AuthorListSerializer, AuthorDetailSerializer
from book.models import Book


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.prefetch_related('books__authors')
    serializer_class = AuthorDetailSerializer

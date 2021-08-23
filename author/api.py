from rest_framework import generics

from author.models import Author
from author.serializers import AuthorListSerializer, AuthorDetailSerializer


class AuthorList(generics.ListAPIView):
    """
    API View for Author List
    """
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer


class AuthorDetail(generics.RetrieveAPIView):
    """
    API View for Details about single Author
    """
    queryset = Author.objects.prefetch_related('books__authors')
    serializer_class = AuthorDetailSerializer

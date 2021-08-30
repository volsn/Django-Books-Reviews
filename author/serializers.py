from rest_framework import serializers

from author.models import Author
from book.serializers import BookSerializer


class AuthorListSerializer(serializers.ModelSerializer):
    """
    Serializer for a List of Authors
    """

    class Meta:
        model = Author
        fields = ('id', 'name',)


class AuthorDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for a single Author
    """
    books = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')

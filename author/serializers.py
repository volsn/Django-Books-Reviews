from rest_framework import serializers
from author.models import Author
import book.serializers


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name',)


class AuthorDetailSerializer(serializers.ModelSerializer):
    books = book.serializers.BookSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')

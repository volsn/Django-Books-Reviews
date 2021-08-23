from rest_framework import serializers
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    def get_authors(self, instance):
        authors = instance.authors.get_queryset()
        return [{'id': author.pk, 'name': author.name}
                for author in authors]

    class Meta:
        model = Book
        fields = ('id', 'title', 'rating', 'publication_year',
                  'description', 'cover_img', 'authors',)

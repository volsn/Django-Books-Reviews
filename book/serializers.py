from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book Model
    """
    authors = serializers.SerializerMethodField()

    def get_authors(self, instance):
        """
        Function used instead of Author List Serializer,
        that can't be used due to circular import
        """
        authors = instance.authors.get_queryset()
        return [{'id': author.pk, 'name': author.name}
                for author in authors]

    class Meta:
        model = Book
        fields = ('id', 'title', 'rating', 'publication_year',
                  'description', 'cover_img', 'authors',)

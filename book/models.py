from django.db import models

from datetime import date

# Create your models here.
from django.db.models import QuerySet


class Book(models.Model):
    """
    Book Model
    """
    title = models.CharField(max_length=256)
    rating = models.FloatField()
    publication_year = models.IntegerField(default=date.today().year)
    cover_img = models.ImageField(upload_to='book_covers', default='book_covers/default.png')
    description = models.TextField()

    authors = models.ManyToManyField('author.Author', blank=True)

    class Meta:
        ordering = ['-rating']  # Sort Books by their descending rating

    def __str__(self) -> str:
        return self.title

    @classmethod
    def find_by_title(cls, title: str) -> QuerySet:
        """
        Return book query by matching title
        :param title: str
        :return: QuerySet
        """
        return cls.objects.filter(title__icontains=title).prefetch_related('authors')

    @classmethod
    def find_by_author(cls, name: str) -> QuerySet:
        """
        Return book query by matching author
        :param name: str
        :return: QuerySet
        """
        return cls.objects.filter(authors__name__contains=name).prefetch_related('authors')

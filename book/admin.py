"""
Registering Models for Django Admin Panel
"""
from django.contrib import admin

from book.models import Book


class BookModel(admin.ModelAdmin):
    """
    Admin Model Setup
    """
    list_filter = ('publication_year', 'authors',)
    search_fields = ('authors', 'title',)


admin.site.register(Book, BookModel)

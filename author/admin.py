"""
Registering Models for Django Admin Panel
"""
from django.contrib import admin
from author.models import Author

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    """
    Admin Model Setup
    """
    search_fields = ('name',)


admin.site.register(Author, AuthorAdmin)

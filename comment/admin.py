"""
Registering Models for Django Admin Panel
"""
from django.contrib import admin

from comment.models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin Model Setup
    """
    list_display = ('title', 'reviewer', 'book',)
    list_filter = ('rating',)
    search_fields = ('title', 'reviewer', 'book',)


class CommentAdmin(admin.ModelAdmin):
    """
    Admin Model Setup
    """
    list_display = ('writer', 'review',)
    search_fields = ('writer', 'review',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)

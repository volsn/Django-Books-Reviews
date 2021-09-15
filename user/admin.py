"""
Registering Models for Django Admin Panel
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Admin Model Setup
    """
    ordering = ('id',)
    list_display = ('email', 'name',)

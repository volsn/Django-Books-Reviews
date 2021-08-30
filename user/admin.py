"""
Registering Models for Django Admin Panel
"""
from django.contrib import admin

from user.models import UserProfileInfo


class UserProfileInfoAdmin(admin.ModelAdmin):
    """
    Admin Model Setup
    """
    ...


admin.site.register(UserProfileInfo, UserProfileInfoAdmin)

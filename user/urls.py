"""
Urls for User App
"""
from django.urls import path
from user.views import user_login, user_logout, user_register

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('register', user_register, name='user_register'),
]

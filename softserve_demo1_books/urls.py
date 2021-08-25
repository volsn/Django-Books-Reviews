"""softserve_demo1_books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

from book.views import index
from user.api import GetToken, RetrieveUser


urlpatterns = [
    path('', index),
    path('book/', include(('book.urls', 'book'), namespace='book')),
    path('accounts/', include(('user.urls', 'user'), namespace='user')),
    path('comment/', include(('comment.urls', 'comment'), namespace='comment')),
    path('api/author/', include('author.urls')),
    path('api/book/', include('book.api')),
    path('api/user/<int:pk>', RetrieveUser.as_view()),
    path('api/login/', GetToken.as_view()),
    path('api-login/', include('rest_framework.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'error_handlers.views.handler403'
handler404 = 'error_handlers.views.handler404'
handler500 = 'error_handlers.views.handler500'

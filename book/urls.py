"""
Url Patterns for Book App
"""
from django.urls import path
from book import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='index'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-details'),
    path('<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),
    path('<int:pk>/update', views.BookUpdateView.as_view(), name='book-update')
]

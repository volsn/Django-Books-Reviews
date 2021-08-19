"""
Url Patterns for Book App
"""
from django.urls import path
from book.views import BooksListView, BookDetailView, BookDeleteView, BookUpdateView


urlpatterns = [
    path('', BooksListView.as_view(), name='index'),
    path('<int:pk>', BookDetailView.as_view(), name='book-details'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book-update')
]

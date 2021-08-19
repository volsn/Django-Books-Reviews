"""
Views for Book App
"""
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  DeleteView, UpdateView)

from book.models import Book
from book.forms import BookForm
from comment.models import Review
from utils.user_utils import ModeratorRequiredMixin

# Create your views here.


class BooksListView(ListView):
    """
    Display all books
    """
    paginate_by = 12
    model = Book
    context_object_name = 'books'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._title = None
        self._author = None

    def setup(self, request, *args, **kwargs):
        """
        Save URL Parameters to Object
        """
        self._title = request.GET.get('title')
        self._author = request.GET.get('author')
        return super().setup(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet:
        """
        Filter queryset by title or author when url parameter is provided,
        otherwise, return default query
        :return: QuerySet
        """
        if self._title:
            return Book.find_by_title(self._title)
        elif self._author:
            return Book.find_by_author(self._author)
        return super().get_queryset().prefetch_related('authors')

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Insert title and author parameters into template context
        """
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = self._title or ''
        context['author'] = self._author or ''
        return context


class BookDetailView(DetailView):
    """
    Details of a single Book
    """
    paginate_by = 12
    model = Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        """
        Insert page number and reviews into template context
        """
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page') or 1
        context['reviews'], context['page_obj'] = Review.get_book_reviews(pk=self.object.pk,
                                                                          page=page,
                                                                          paginate_by=self.paginate_by)
        return context


class BookDeleteView(ModeratorRequiredMixin, DeleteView):
    """
    Delete Book View. Only available to moderator or superuser
    """
    model = Book
    success_url = reverse_lazy('book:index')


class BookUpdateView(ModeratorRequiredMixin, UpdateView):
    """
    Update Book View. Only available to moderator or superuser
    """
    model = Book
    form_class = BookForm
    context_object_name = 'book'

    def get_success_url(self):
        """
        Return User to Book Details Page
        """
        return reverse_lazy('book:book-details', kwargs={'pk': self.kwargs.get('pk')})

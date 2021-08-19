from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    """
    Django Form for Book Model used when creating or updating Book objects
    """
    class Meta:
        model = Book
        fields = ('title', 'rating', 'publication_year', 'cover_img', 'description',)

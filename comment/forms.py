from django.forms import ModelForm
from django.forms.widgets import Textarea
from comment.models import Review, Comment


class ReviewForm(ModelForm):
    """
    Django Form for Review Model used when creating or updating Review objects
    """
    class Meta:
        model = Review
        fields = ['title', 'text', 'rating']


class CommentForm(ModelForm):
    """
    Django Form for Comment Model used when creating or updating Comment objects
    """
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'text': Textarea}

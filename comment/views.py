from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, DetailView,
                                  UpdateView, DeleteView)
from django.http import HttpResponseRedirect

from comment.models import Review, Comment
from comment.forms import ReviewForm, CommentForm

from utils.user_utils import (OwnerOrModeratorRequiredMixin, LoginRequiredMixin,
                              current_user_is_moderator)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    Create Review
    """
    model = Review
    form_class = ReviewForm
    template_name = 'comment/review_form.html'

    def get_context_data(self, **kwargs):
        """
        Insert submit url and submit button text into template context.
        Needed because we use the same template for updating and creating reviews.
        """
        context = super().get_context_data(**kwargs)
        context['submit_url'] = reverse_lazy('comment:review-add', kwargs={'pk': self.kwargs.get('pk')})
        context['submit_text'] = 'Add Review'
        return context

    def form_valid(self, form):
        """
        Add Book id and Reviewer id fields to object before saving it.
        """
        review = Review(title=form.cleaned_data['title'],
                        text=form.cleaned_data['text'],
                        rating=form.cleaned_data['rating'])
        review.book_id = self.kwargs.get('pk')
        review.reviewer_id = self.request.user.pk
        review.save()
        return HttpResponseRedirect(reverse('book:book-details',
                                            kwargs={'pk': self.kwargs.get('pk')}))


class ReviewDetailView(DetailView):
    """
    Review Details
    """
    model = Review
    paginate_by = 12
    context_object_name = 'review'
    template_name = 'comment/review_detail.html'

    def get_queryset(self):
        """
        Select Related Book for better performance
        """
        return super().get_queryset().select_related('book')

    def get_context_data(self, **kwargs):
        """
        Insert page number and comments into template context
        """
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page') or 1
        context['comments'], context['page_obj'] = Comment.get_review_comments(pk=self.object.pk,
                                                                               page=page,
                                                                               paginate_by=self.paginate_by)
        context['current_user_is_moderator'] = current_user_is_moderator(self.request)
        return context


class ReviewUpdateView(OwnerOrModeratorRequiredMixin, UpdateView):
    """
    Review Update
    """
    model = Review
    form_class = ReviewForm
    template_name = 'comment/review_form.html'

    def get_context_data(self, **kwargs):
        """
        Insert submit url and submit button text into template context.
        Needed because we use the same template for updating and creating reviews.
        """
        context = super().get_context_data(**kwargs)
        context['submit_url'] = reverse_lazy('comment:review-update', kwargs={'pk': self.kwargs.get('pk')})
        context['submit_text'] = 'Update Review'
        return context

    def get_success_url(self):
        """
        Return User to Review Details page
        """
        return reverse_lazy('comment:review-details', kwargs={'pk': self.kwargs.get('pk')})


class ReviewDeleteView(OwnerOrModeratorRequiredMixin, DeleteView):
    """
    Review Delete. Only available for superuser, moderator and review owner
    """
    model = Review

    def get_success_url(self):
        """
        Return User to Book Details Page
        """
        return reverse_lazy('book:book-details', kwargs={'pk': self.object.book_id})


class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Comment Create
    """
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_form.html'

    def get_context_data(self, **kwargs):
        """
        Insert submit url and submit button text into template context.
        Needed because we use the same template for updating and creating comments.
        """
        context = super().get_context_data(**kwargs)
        context['submit_url'] = reverse_lazy('comment:comment-add', kwargs={
            'pk': self.kwargs.get('pk'),
            'reply_to': self.kwargs.get('reply_to')
        })
        context['submit_text'] = 'Add Comment'
        return context

    def form_valid(self, form):
        """
        Add Writer id and Reviewer id fields to object before saving it.
        """
        comment = Comment(text=form.cleaned_data['text'])
        comment.writer_id = self.request.user.pk
        comment.review_id = self.kwargs.get('pk')
        if self.kwargs.get('reply_to') != 'None':
            comment.replied_to_id = self.kwargs.get('reply_to')
        comment.save()
        return HttpResponseRedirect(reverse('comment:review-details',
                                            kwargs={'pk': self.kwargs.get('pk')}))


class CommentUpdateView(OwnerOrModeratorRequiredMixin, UpdateView):
    """
    Comment Update. Only available for superuser, moderator and review owner
    """
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_form.html'

    def get_context_data(self, **kwargs):
        """
        Insert submit url and submit button text into template context.
        Needed because we use the same template for updating and creating comments.
        """
        context = super().get_context_data(**kwargs)
        context['submit_url'] = reverse_lazy('comment:comment-update', kwargs={'pk': self.kwargs.get('pk')})
        context['submit_text'] = 'Update Comment'
        return context

    def get_success_url(self):
        """
        Return User to Review Details Page
        """
        return reverse_lazy('comment:review-details', kwargs={'pk': self.object.review_id})


class CommentDeleteView(OwnerOrModeratorRequiredMixin, DeleteView):
    """
    Comment Delete. Only available for superuser, moderator and review owner
    """
    model = Comment
    context_object_name = 'comment'

    def get_success_url(self):
        """
        Return User to Review Details Page
        """
        return reverse_lazy('comment:review-details', kwargs={'pk': self.object.review_id})

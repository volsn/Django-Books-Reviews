"""
Urls for Comment App
"""
from django.contrib.auth.decorators import login_required
from django.urls import path
from comment.views import (ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView,
                           CommentUpdateView, CommentCreateView, CommentDeleteView)

urlpatterns = [
    path('<int:pk>/review/add', login_required(ReviewCreateView.as_view()), name='review-add'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review-details'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review-delete'),
    path('review/<int:pk>/comment/add/<reply_to>', login_required(CommentCreateView.as_view()), name='comment-add'),
    path('<int:pk>/update', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
]

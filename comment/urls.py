"""
Urls for Comment App
"""
from django.urls import path
from comment import views

urlpatterns = [
    path('<int:pk>/review/add', views.ReviewCreateView.as_view(), name='review-add'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review-details'),
    path('review/<int:pk>/update', views.ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete', views.ReviewDeleteView.as_view(), name='review-delete'),
    path('review/<int:pk>/comment/add/<reply_to>', views.CommentCreateView.as_view(), name='comment-add'),
    path('<int:pk>/update', views.CommentUpdateView.as_view(), name='comment-update'),
    path('<int:pk>/delete', views.CommentDeleteView.as_view(), name='comment-delete'),
]

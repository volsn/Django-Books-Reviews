from django.urls import path
from author.api import AuthorList, AuthorDetail

urlpatterns = [
    path('', AuthorList.as_view(), name='api-author-list'),
    path('<int:pk>', AuthorDetail.as_view(), name='api-author-detail')
]

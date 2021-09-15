from typing import Tuple

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import models
from django.db.models import QuerySet


class Review(models.Model):
    """
    Review Model
    """

    RATING_CHOICES = zip(range(1, 6), range(1, 6))

    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)

    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)

    approved = models.BooleanField(default=False)

    def __repr__(self) -> str:
        """
        Repr method overriding
        :return: str
        """
        return self.reviewer.username + ' : ' + self.book.title

    def __str__(self) -> str:
        """
        Str method overriding
        :return: str
        """
        return self.title

    @property
    def intro(self) -> str:
        """
        Review Intro displayed in Book Details View
        :return: str
        """
        return self.text[:100] + '...'

    @property
    def owner(self) -> User:
        """
        Property for accessing the user who wrote the review.
        Added for compatibility with Comment model.
        :return: User
        """
        return self.reviewer

    def save(self, *args, **kwargs):
        """
        All comments written by superuser or moderator are approved by default
        """
        if self.reviewer.is_superuser or self.reviewer.groups.filter(
                name='moderator').exists():
            self.approved = True
        super().save(*args, **kwargs)

    @classmethod
    def get_book_reviews(cls, *, pk: int, page: int = 0,
                         paginate_by: int = 12) -> Tuple[QuerySet, Paginator]:
        """
        Return Book Reviews and Pagination object.
        Used in Book Details view.
        :param pk: int
        :param page: int = 0
        :param paginate_by: int = 12
        :return: Tuple[QuerySet, Paginator]
        """
        pag = Paginator(
            cls.objects.select_related('reviewer').filter(approved=True,
                                                          book__pk=pk),
            paginate_by)
        return pag.page(page).object_list, pag


class Comment(models.Model):
    """
    Comment Model
    """

    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.ForeignKey('comment.Review', on_delete=models.CASCADE)
    replied_to = models.ForeignKey('comment.Comment', on_delete=models.CASCADE,
                                   null=True, blank=True, default=None)
    text = models.CharField(max_length=1024)
    approved = models.BooleanField(default=False)

    @property
    def owner(self) -> User:
        """
        Property for accessing the user who wrote the review.
        Added for compatibility with Review model.
        :return: User
        """
        return self.writer

    def __repr__(self) -> str:
        """
        Repr method overriding
        :return: str
        """
        return self.writer.username + " : " + str(self.review.pk)

    def __str__(self) -> str:
        """
        Str method overriding
        :return: str
        """
        return self.text[:100]

    def save(self, *args, **kwargs):
        """
        All comments written by superuser or moderator are approved by default
        """
        if self.writer.is_superuser or self.writer.groups.filter(
                name='moderator').exists():
            self.approved = True
        super().save(*args, **kwargs)

    @classmethod
    def get_review_comments(cls, *, pk: int, page: int = 0,
                            paginate_by: int = 12) \
            -> Tuple[QuerySet, Paginator]:
        """
        Return Review Comments and Pagination object.
        Used in Book Reviews view.
        :param pk: int
        :param page: int = 0
        :param paginate_by: int = 12
        :return: Tuple[QuerySet, Paginator]
        """
        pag = Paginator(cls.objects.prefetch_related('writer')
                        .filter(approved=True, review__pk=pk), paginate_by)
        return pag.page(page).object_list, pag

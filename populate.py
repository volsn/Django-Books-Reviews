import os
import pickle
import random

import pandas as pd
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'softserve_demo1_books.settings')

import django

django.setup()

from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password

from author.models import Author
from book.models import Book
from user.models import User
from comment.models import Review, Comment

fake = Faker()


def load_authors(path=os.path.join('data', 'authors.pickle')):
    with open(path, 'rb') as file:
        authors = pickle.load(file)

    for name in authors:
        try:
            author = Author(name=name)
            author.save()
        except IntegrityError:
            pass


def load_books(path=os.path.join('data', 'books_cleaned.csv')):
    books = pd.read_csv(path, index_col=None)
    for _, book_details in books.iterrows():
        try:
            authors = book_details.pop('authors')
            book_details['description'] = fake.text(2048)
            book = Book(**book_details)
            book.save()
            for author in authors.split(', '):
                book.authors.add(Author.objects.filter(name=author).first())
            book.save()

            generate_reviews(book)
        except IntegrityError:
            pass


def generate_users(num=100):
    for _ in range(num):
        user = User(username=fake.profile()['username'],
                    password=make_password(fake.password()))
        user.save()


def generate_reviews(book):
    for _ in range(random.randint(1, 12)):
        review = Review(
            reviewer_id=User.objects.order_by('?').first().pk,
            book_id=book.pk,
            title=fake.sentence(),
            text=fake.text(256),
            rating=random.randint(2, 5),
            approved=True
        )
        review.save()
        generate_comments(review)


def generate_comments(review):
    for _ in range(random.randint(1, 4)):
        comment = Comment(
            writer=User.objects.order_by('?').first(),
            review_id=review.pk,
            text=fake.text(128),
            approved=True
        )
        comment.save()


if __name__ == '__main__':
    generate_users()
    load_authors()
    load_books()

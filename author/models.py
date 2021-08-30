from django.db import models


class Author(models.Model):
    """
    Author Model
    """
    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.name

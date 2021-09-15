from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    """
    Manager for user model
    """

    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a new user
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a new superuser
        """
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    portfolio_pic = models.ImageField(upload_to='profile_pics',
                                      blank=True,
                                      default='profile_pics/default.png')

    objects = UserManager()

    USERNAME_FIELD = 'email'

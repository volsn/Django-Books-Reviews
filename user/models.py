from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    """
    Custom Model that ads Profile Picture to User
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/default.png')

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = 'Profile'

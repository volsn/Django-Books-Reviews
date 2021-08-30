from typing import Union

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.http import HttpRequest


class MyCustomAuthBackend(BaseBackend):
    """
    Custom Authentication Backend
    """

    def authenticate(self, request: HttpRequest, username: str = None,
                     password: str = None) -> Union[User, None]:
        """
        Overriding authenticate method.
        Return User object when correct username and password provided,
        otherwise, return None.

        :param request: HttpRequest
        :param username: str = None
        :param password: str = None
        :return: Union[User, None]
        """
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass

        return None

    def get_user(self, user_id: int) -> Union[User, None]:
        """
        Overriding get_user method.
        Return User object when user with given id exists or None otherwise.

        :param user_id: int
        :return: Union[User, None]
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

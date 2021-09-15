from typing import Union

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpRequest


class MyCustomAuthBackend(BaseBackend):
    """
    Custom Authentication Backend
    """

    def authenticate(self, request: HttpRequest, email: str = None,
                     password: str = None) -> Union[User, None]:
        """
        Overriding authenticate method.
        Return User object when correct username and password provided,
        otherwise, return None.

        :param request: HttpRequest
        :param email: str = None
        :param password: str = None
        :return: Union[User, None]
        """
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
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
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

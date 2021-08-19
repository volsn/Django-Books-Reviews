from functools import wraps

from django.http import HttpResponseForbidden


def current_user_is_moderator(request):
    return request.user.is_authenticated and (request.user.groups.filter(name='moderator').exists()
                                              or request.user.is_superuser)


def moderator_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.request.user.is_authenticated and (self.request.user.groups.filter(name='moderator').exists()
                                                   or self.request.user.is_superuser):
            return func(self, *args, **kwargs)
        return HttpResponseForbidden("Cannot delete other's posts")
    return wrapper


def owner_or_moderator_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.request.user.is_authenticated and (self.request.user.groups.filter(name='moderator').exists()
                                                   or self.request.user.is_superuser
                                                   or self.object.owner.pk == self.request.user.pk):
            return func(self, *args, **kwargs)
        return HttpResponseForbidden("Cannot delete other's posts")
    return wrapper


class ModeratorRequiredMixin:
    @moderator_required
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class OwnerOrModeratorRequiredMixin:
    @owner_or_moderator_required
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

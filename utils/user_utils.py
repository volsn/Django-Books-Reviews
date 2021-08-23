from functools import wraps

from django.http import HttpResponseForbidden


def current_user_is_moderator(request):
    return request.user.is_authenticated and (request.user.groups.filter(name='moderator').exists()
                                              or request.user.is_superuser)


class ModeratorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser \
                or request.user.groups.filter(name='moderator').exists():
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()


class OwnerOrModeratorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='moderator').exists()
                or request.user.is_superuser
                or self.object.owner.pk == request.user.pk):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden()

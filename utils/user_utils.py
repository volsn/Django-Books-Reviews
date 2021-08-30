from django.http import HttpResponseForbidden


def current_user_is_moderator(request):
    return request.user.groups.filter(name='moderator').exists() \
           or request.user.is_superuser


class ModeratorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if current_user_is_moderator(request):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('Moderator Rights required')


class OwnerOrModeratorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if (current_user_is_moderator(request)
                or self.object.owner.pk == request.user.pk):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('Moderator or Owner Rights required')


class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('Login Required')

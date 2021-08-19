from django import template

register = template.Library()


@register.filter
def is_moderator(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name='moderator').exists())

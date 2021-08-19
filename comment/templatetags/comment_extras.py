from django import template

register = template.Library()


@register.filter
def first_child(comments):
    output = []
    for comment in comments:
        if comment.replied_to is None:
            output.append(comment)
    return output


@register.filter
def children(comments, comment_parent):
    output = []
    for comment in comments:
        if comment.replied_to and comment.replied_to.pk == comment_parent.pk:
            output.append(comment)
    return output

from django.shortcuts import render

# Create your views here.


def handler403(request, *args, **kwargs):
    """
    Permission Denied Handler
    """
    response = render(request, 'error_handlers/403.html')
    response.status_code = 404
    return response


def handler404(request, *args, **kwargs):
    """
    Page Not Found Handler
    """
    response = render(request, 'error_handlers/404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **kwargs):
    """
    Internal Server Error Handler
    """
    response = render(request, 'error_handlers/500.html')
    response.status_code = 404
    return response

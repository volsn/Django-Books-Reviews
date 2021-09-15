from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserForm


def user_login(request):
    """
    Login View
    """

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('book:index'))
            else:
                return HttpResponseForbidden('Login Failed')

        else:
            return HttpResponseForbidden('Login Failed')
    else:
        return render(request, 'user/login.html', context={})


def user_register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)

            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']

            user.save()

            registered = True

    else:

        user_form = UserForm()

    return render(request, 'user/user_form.html',
                  context={
                      'user_form': user_form,
                      'registered': registered
                  })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('book:index'))

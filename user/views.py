from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden

from user.forms import UserForm, UserProfileInfoForm


def user_login(request):
    """
    Login View
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

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
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

    else:

        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user/user_form.html',
                  context={
                      'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered
                  })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('book:index'))

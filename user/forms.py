from django import forms
from django.contrib.auth.models import User
from user.models import UserProfileInfo


class UserForm(forms.ModelForm):
    """
    Form for Django built in User Model
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    """
    Form for my custom model that ads profile picture to user
    """
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_pic',)

from django import forms

from user.models import User


class UserForm(forms.ModelForm):
    """
    Form for Django built in User Model
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password', 'portfolio_pic',)

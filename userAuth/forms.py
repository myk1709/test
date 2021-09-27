from django import forms
from django.contrib.auth.models import User
from userAuth.models import UserSignIn


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfo(forms.ModelForm):

    class Meta:
        model = UserSignIn
        fields = ('portfolio_site', 'profile_pic')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from users.models import Profile


class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    username = forms.CharField(label="Nombre de Usuario")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class ProfileForm(ModelForm):

    info = forms.Textarea()

    class Meta:
        model = Profile
        fields = ['info', 'img']
        exclude = ['user']


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())



from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from users.models import Profile


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    username = forms.CharField(label="Nombre de Usuario")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']



class ProfileForm(ModelForm):

    class Meta:

        model = Profile
        fields = ['info', 'img', 'user']

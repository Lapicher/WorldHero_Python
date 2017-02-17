# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext as _

from users.models import Profile


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileForm(ModelForm):

    info = forms.Textarea()

    class Meta:
        model = Profile
        fields = ['info', 'img']
        exclude = ['user']


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Nombre de Usuario"))
    pwd = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput())



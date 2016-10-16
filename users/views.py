from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from pip._vendor.requests import Response

from users.forms import UserForm, ProfileForm, LoginForm
from users.models import Profile


class UserRegisterView(View):

    def get(self, request):
        """
        Presenta el formulario para crear usuario nuevo
        :param request:
        :return:
        """
        message = ""
        user_form = UserForm()
        context = {'form': user_form, 'message': message}
        return render(request, 'users/register.html', context)

    def post(self, request):
        """
        Peticion POST para crear al usuario.
        :param request:
        :return:
        """

        message = ""
        user = User()

        user_form = UserForm(request.POST, instance=user)
        contrasena = user_form.data.get('password')

        if user_form.is_valid():
            new_user = user_form.save()
            user_form = UserForm()  # limpia los campos para que se pueda crear una nueva foto.
            message = "Usuario creada satisfactoriamente, Iniciar Sesion"

        context = {'form': user_form, 'message': message}
        return render(request, 'users/register.html', context)

class ActualizarUser(View):
    @method_decorator(login_required())
    def post(self, request, user):
        """
        Actualiza el Perfil del usuario, imagen de perfil e informacion acerca del usuario.
        :param request:
        :return:
        """

        message = ""

        if request.is_ajax():
            #usuario_owner = User(pk=request.user)
            profile_of_user = Profile(user=request.user)
            form = ProfileForm(request.POST, request.FILES, instance=profile_of_user)

            if form.is_valid():
                form.save()
                return HttpResponse(
                    "Usuario Actualizado Correctamente", content_type="text/plain"
                )
            else:
                message = "Formulario Invalido"
        else:
            message = "La solicitud no es Ajax"

        return HttpResponseBadRequest(message)



class LoginView(View):
    def get(self, request):
        """
        Renderiza la plantilla de Login para el usuario.
        :param request:
        :return:
        """

        error_messages = ""
        login_form = LoginForm()
        context = {'error': error_messages, 'form': login_form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Gestiona el login del usuario
        :param request:
        :return:
        """

        error_messages = ""
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')

            user = authenticate(username=username, password=password)
            if user is None:
                error_messages = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'blog_home'))
                else:
                    error_messages = "Cuenta de usuario inactiva"

        context = {'error': error_messages, 'form': login_form}
        return render(request, 'users/login.html', context)


class LogoutView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
        Hace el logout de un usuario redirige al login
        :param request:
        :return:
        """
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('blog_home')
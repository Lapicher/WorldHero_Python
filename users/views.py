from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from pip._vendor.requests import Response

from users.forms import UserForm, ProfileForm


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

        if user_form.is_valid():
            new_user = user_form.save()
            user_form = UserForm()  # limpia los campos para que se pueda crear una nueva foto.
            message = "Usuario creada satisfactoriamente <a href='{0}'> Ver foto {1} </a>".format(
                # reverse('photos_detail', args=[new_user.pk, new_user.username])
                1, new_user.username
            )

        context = {'form': user_form, 'message': message}
        return render(request, 'users/register.html', context)

class ActualizarUser(View):

    def post(self, request, user):
        """
        Actualiza el Perfil del usuario, imagen de perfil e informacion acerca del usuario.
        :param request:
        :return:
        """

        message = ""

        if request.is_ajax():
            usuario_owner = User(pk=request.POST.get('user'))
            form = ProfileForm(request.POST, request.FILES, user=request.user)

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

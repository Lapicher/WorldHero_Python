from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.datetime_safe import datetime
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blog.models import Blog, VISIBILITY_PUBLIC, VISIBILITY_PRIVATE
from blog.serializers import BlogSerializer, BlogListSerializer
from users.permissions import UserPermissionBlog


class BlogViewSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly, UserPermissionBlog, )
    search_fields = ('title', 'body', )
    order_fields = ('-datePub', 'title', )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )


    def get_queryset(self):


        blogs = Blog.objects.all().select_related("owner").order_by('-datePub')

        if self.request.user.is_superuser:
            # como administrador obtiene todos los posts.
            return blogs
        elif self.request.user.is_authenticated():
            # no obtiene los posts que esten privados de otros usuarios. y solo los publicados hasta al dia de hoy.
            blogs = blogs.filter(datePub__lte=datetime.today())
            return blogs.exclude(Q(visibility=VISIBILITY_PRIVATE) & ~Q(owner=self.request.user))

        else:
            # invitado prodra ver los posts publicos.
            return blogs.filter(datePub__lte=datetime.today(), visibility=VISIBILITY_PUBLIC)

    # se comenta la linea anterior para permitir al metodo siguiente seleccionar que serializador escoger.
    def get_serializer_class(self):

        if self.action != 'list':
            serializador = BlogSerializer
        else:
            serializador = BlogListSerializer

        return serializador


    # metodo que nos sirve para crear la foto con el propietario que se logueo en la API.

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # metodo para que al modificar solo se modifique la foto propietaria del usuario autentificado.
    def perform_update(self, serializer):

        # si el administrador va a actualizar, el propietario del post será el que él elija por medio de la llave owner.
        propietario = self.request.user
        if self.request.user.is_superuser:
            propietario = get_object_or_404(User, username=self.request.data.get('owner'))
        return serializer.save(owner=propietario)


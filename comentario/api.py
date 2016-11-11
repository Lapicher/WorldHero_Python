from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.datetime_safe import datetime
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blog.models import Blog, VISIBILITY_PUBLIC, VISIBILITY_PRIVATE
from blog.serializers import BlogSerializer, BlogListSerializer
from blog.util import generate_responsive_images, find_hashtags, send_mail
from comentario.models import Comment
from users.permissions import UserPermissionBlog
from comentario.serializer import CommentListSerializer


class CommentViewSet(ModelViewSet):

    # permission_classes = (IsAuthenticatedOrReadOnly )
    # search_fields = ('owner', 'text', )
    # order_fields = ('-created_at', )
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter, )


    def get_queryset(self):

        """
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
        """
        comments = Comment.objects.all()
        return comments

    # se comenta la linea anterior para permitir al metodo siguiente seleccionar que serializador escoger.
    def get_serializer_class(self):

        if self.action != 'list':
            serializador = CommentViewSet
        else:
            serializador = CommentListSerializer

        return serializador


    # metodo que nos sirve para crear la foto con el propietario que se logueo en la API.

    def perform_create(self, serializer):

        post = None
        return  post

    # metodo para que al modificar solo se modifique la foto propietaria del usuario autentificado.
    def perform_update(self, serializer):

        post = None
        return post


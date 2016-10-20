from django.utils.datetime_safe import datetime
from rest_framework import filters
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blog.models import Blog
from blog.serializers import BlogSerializer, BlogListSerializer



class BlogViewSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    search_fields = ('title', 'body', )
    order_fields = ('-datePub', 'title', )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Blog.objects.all().select_related("owner").filter(owner=self.request.user)
        elif self.request.user.is_superuser:
            return Blog.objects.all().select_related("owner")
        else:
            return Blog.objects.all().selected_related("owner").filter(datePub__lte=datetime.today())

    # se comenta la linea anterior para permitir al metodo siguiente seleccionar que serializador escoger.
    def get_serializer_class(self):
        return BlogSerializer if self.action != 'list' else BlogListSerializer

    # metodo que nos sirve para crear la foto con el propietario que se logueo en la API.

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # metodo para que al modificar solo se modifique la foto propietaria del usuario autentificado.
    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
"""
    def create(self, request, *args, **kwargs):
        uv = Blog(owner=self.request.user)
        serializer = self.serializer_class(uv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""



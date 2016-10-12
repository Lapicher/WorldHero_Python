from django.forms import ModelForm
from django import forms

from blog.models import Blog


class BlogForm(ModelForm):
    title = forms.CharField(label="Titulo")
    intro = forms.CharField(label="Introducción")
    # body = forms.Textarea()
    # image = forms.ImageField(label="Imagen de Cabecera")
    datePub = forms.DateField(label="Fecha de Publicacion")


    class Meta:
        model = Blog
        fields = ['title', 'intro', 'body', 'image', 'datePub', 'type']
        exclude = ['owner']


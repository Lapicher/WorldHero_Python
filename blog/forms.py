# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext as _

from blog.models import Blog


class BlogForm(ModelForm):
    title = forms.CharField(label=_("Titulo"))
    intro = forms.CharField(label=_("Introducción"))
    # body = forms.Textarea()
    # image = forms.ImageField(label="Imagen de Cabecera")
    datePub = forms.DateField(label=_("Fecha de Publicación"))

    class Meta:
        model = Blog
        fields = ['title', 'intro', 'body', 'image', 'datePub', 'type', 'visibility', ]
        exclude = ['owner']


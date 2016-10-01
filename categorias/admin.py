from django.contrib import admin

# Register your models here.

from categorias.models import Category

admin.site.register(Category)

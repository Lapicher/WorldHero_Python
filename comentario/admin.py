from django.contrib import admin

# Register your models here.
from comentario.models import Comment

admin.site.register(Comment)
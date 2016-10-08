from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from categorias.models import Category


class Blog(models.Model):

    owner = models.ForeignKey(User)
    type = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads', null=True)
    datePub = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



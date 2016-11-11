from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from blog.models import Blog


class Comment(models.Model):

    blog = models.ForeignKey(Blog)
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.owner.username
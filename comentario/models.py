from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from blog.models import Blog


class Comment(models.Model):

    #blog = models.CharField(null=True, max_length=150)
    blog = models.ForeignKey(Blog, blank=True, null=True)
    owner = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.owner.username
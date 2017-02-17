# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):

    info = models.TextField(max_length=30, null=True)
    user = models.OneToOneField(User)
    img = models.ImageField(upload_to='uploads/profiles', null=True)


from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from easy_thumbnails.fields import ThumbnailerImageField

from blog.settings import DEFAULT_IMAGE_OPTIONS
from categorias.models import Category


VISIBILITY_PUBLIC = "PUB"
VISIBILITY_PRIVATE = "PRI"

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Publica'),
    (VISIBILITY_PRIVATE, 'Privada')
)


class Blog(models.Model):

    owner = models.ForeignKey(User)
    type = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=400)
    body = models.TextField()
    image = ThumbnailerImageField(upload_to='uploads', null=True, resize_source=DEFAULT_IMAGE_OPTIONS)
    datePub = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    def __str__(self):
        return self.title



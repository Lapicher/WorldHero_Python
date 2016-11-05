from django.core.management import BaseCommand

from blog.models import Blog
from blog.util import generate_responsive_images


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Fetching post to resize its images")
        blogs = Blog.objects.filter(image_resized=False)
        print("{0} posts to resize".format(blogs.count()))
        for blog in blogs:
            print("Resizing post {0}".format(blog.pk))
            generate_responsive_images(blog)
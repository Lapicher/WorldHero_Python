from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Blog


class BlogListSerializer(BlogSerializer):

    class Meta:
        model = Blog
        fields = ("title", "image", "intro", "datePub", "owner", )

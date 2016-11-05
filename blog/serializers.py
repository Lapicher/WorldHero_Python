from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(
        default=serializers.CurrentUserDefault()
    )

    # image = serializers.CharField(validators=[formatURLImage])
    image = serializers.ImageField()

    class Meta:
        model = Blog


class BlogListSerializer(BlogSerializer):

    class Meta:
        model = Blog
        fields = ("title", "image", "intro", "datePub", )


class BlogDetailSerializer(BlogSerializer):

    class Meta:
        model = Blog
        fields = ("title", "intro")

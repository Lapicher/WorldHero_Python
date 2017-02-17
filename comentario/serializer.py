from rest_framework import serializers

from blog.models import Blog
from comentario.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment


class CommentListSerializer(CommentSerializer):

    owner = serializers.CharField()

    class Meta:
        model = Comment
        fields = ("owner", "blog", "text", "created_at", )



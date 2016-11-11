from rest_framework import serializers

from comentario.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment


class CommentListSerializer(CommentSerializer):

    class Meta:
        model = Comment
        fields = ("owner", "blog", "text", "created_at", )



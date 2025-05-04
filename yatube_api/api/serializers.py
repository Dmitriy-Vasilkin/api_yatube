from rest_framework import serializers

from api.constants import AUTHOR_SLUG_FIELD_PARAMS
from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post."""

    author = serializers.SlugRelatedField(**AUTHOR_SLUG_FIELD_PARAMS)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment."""

    author = serializers.SlugRelatedField(**AUTHOR_SLUG_FIELD_PARAMS)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)

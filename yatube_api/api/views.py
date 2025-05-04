from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAuthor
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет Comment."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.get_post().comments.all()

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

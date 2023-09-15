from django.shortcuts import render
from rest_framework import generics, permissions

from post.models import Post
from post.serializers import PostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
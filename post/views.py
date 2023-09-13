from django.shortcuts import render
from rest_framework import generics

from post.models import Post
from post.serializers import PostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

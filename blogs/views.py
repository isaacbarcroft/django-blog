from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from accounts.models import User


class BlogList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

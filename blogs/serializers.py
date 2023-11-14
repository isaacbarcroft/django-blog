from rest_framework import serializers
from .models import Blog
from accounts.models import User


class BlogSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    created_at = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at', 'user_name', 'user')

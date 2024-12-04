from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Tag, Comment, BlogPost


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]


class SimpleTagSerializer(serializers.Serializer):
    name = serializers.CharField()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at"]


class BlogPostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    author = UserSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tags = SimpleTagSerializer(many=True)


class BlogPostCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    tags = SimpleTagSerializer(many=True, required=False)

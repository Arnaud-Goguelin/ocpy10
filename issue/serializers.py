from rest_framework.serializers import ModelSerializer

from .models import Comment, Issue


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ["title", "content", "status", "priority", "tags", "created_at", "project", "author", "assigned_users"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["title", "content", "author", "created_at"]

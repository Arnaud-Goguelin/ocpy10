from rest_framework.serializers import ModelSerializer

from .models import Issue


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ["title", "content", "status", "priority", "tags", "created_at", "project", "author", "assigned_users"]

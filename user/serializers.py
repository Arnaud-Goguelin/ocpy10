from rest_framework.serializers import IntegerField, ModelSerializer, Serializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class ContributorSerializer(Serializer):
    """Serializer for adding a contributor to a project"""

    user_id = IntegerField(required=True, help_text="ID of the user to add as contributor")

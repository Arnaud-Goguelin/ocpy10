from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from .models import Comment, Issue
from .serializers import CommentSerializer, IssueSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get all Issues",
        tags=["Issue"],
    ),
    retrieve=extend_schema(
        summary="Get an Issue",
        tags=["Issue"],
    ),
    create=extend_schema(
        summary="Create an Issue",
        tags=["Issue"],
    ),
    update=extend_schema(
        summary="Update entirely an Issue",
        tags=["Issue"],
    ),
    partial_update=extend_schema(
        summary="Update one or many Issue's fields",
        tags=["Issue"],
    ),
    destroy=extend_schema(
        summary="Delete an Issue",
        tags=["Issue"],
    ),
)
class IssueModelViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = []


@extend_schema_view(
    list=extend_schema(
        summary="Get all Comments",
        tags=["Comment"],
    ),
    retrieve=extend_schema(
        summary="Get an Comment",
        tags=["Comment"],
    ),
    create=extend_schema(
        summary="Create an Comment",
        tags=["Comment"],
    ),
    update=extend_schema(
        summary="Update entirely an Comment",
        tags=["Comment"],
    ),
    partial_update=extend_schema(
        summary="Update one or many Comment's fields",
        tags=["Comment"],
    ),
    destroy=extend_schema(
        summary="Delete an Comment",
        tags=["Comment"],
    ),
)
class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

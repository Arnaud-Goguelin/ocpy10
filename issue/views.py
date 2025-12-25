from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from .models import Issue
from .serializers import IssueSerializer


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

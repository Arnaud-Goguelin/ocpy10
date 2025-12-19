from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from project.models import Project
from user.models import User
from user.serializers import ContributorSerializer, UserSerializer

from .serializers import ProjectSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get all Projects",
        tags=["Project"],
    ),
    retrieve=extend_schema(
        summary="Get a Project",
        tags=["Project"],
    ),
    create=extend_schema(
        summary="Create a Project",
        tags=["Project"],
    ),
    update=extend_schema(
        summary="Update entirely a Project",
        tags=["Project"],
    ),
    partial_update=extend_schema(
        summary="Update one or many Project's fields",
        tags=["Project"],
    ),
    destroy=extend_schema(
        summary="Delete Project",
        tags=["Project"],
    ),
)
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []

    @extend_schema(
        methods=["GET"],
        summary="List all contributors of a Project",
        description="Returns the list of all users who are contributors to this Project.",
        tags=["Project Contributors"],
        responses={200: UserSerializer(many=True)},
    )
    @extend_schema(
        methods=["POST"],
        summary="Add a contributor to a Project",
        description="Add a user as a contributor to this Project.",
        tags=["Project Contributors"],
        request=ContributorSerializer,
        responses={
            201: {"description": "Contributor added successfully"},
            400: {"description": "Bad request - user_id missing or user already a contributor"},
        },
    )
    @action(detail=True, methods=["get", "post"], url_path="contributors")
    def contributors(self, request, pk=None):
        """
        GET: List all contributors of a project
        <br>POST: Add a contributor to a project
        <br>
        <br>**Authentification required**: Yes
        <br>**Permissions required**: None
        """
        project = self.get_object()

        if request.method == "GET":
            return self._list_contributors(project)
        elif request.method == "POST":
            return self._add_contributor(project, request)

    def _list_contributors(self, project):
        """Private method to handle GET logic"""
        contributors = project.contributors.all()
        serializer = UserSerializer(contributors, many=True)
        return Response(serializer.data)

    def _add_contributor(self, project, request):
        """Private method to handle POST logic"""
        serializer = ContributorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data["user_id"]

        user = get_object_or_404(User, pk=user_id)

        if user in project.contributors.all():
            return Response({"error": "User is already a contributor"}, status=400)

        project.contributors.add(user)
        return Response({"message": f"User {user.username} added as contributor"}, status=201)

    @extend_schema(
        methods=["DELETE"],
        summary="Pop a contributor to a Project",
        description="Remove a user from this Project's contributor.",
        tags=["Project Contributors"],
        parameters=[
            OpenApiParameter(
                name="user_id",
                type=OpenApiTypes.INT,
                location="path",
                description="ID of the user to remove from contributors",
                required=True,
            )
        ],
    )
    @action(detail=True, methods=["delete"], url_path="contributors/(?P<user_id>[^/.]+)")
    def remove_contributor(self, request, pk=None, user_id=None):
        """
        Remove a specific contributor from a project
        <br>
        <br>**Authentification required**: Yes
        <br>**Permissions required**: None
        """

        if not user_id:
            return Response({"error": "user_id is required in url"}, status=400)

        project = self.get_object()

        user = get_object_or_404(User, pk=user_id)

        if user not in project.contributors.all():
            return Response({"error": "User is not a contributor of this project"}, status=400)

        project.contributors.remove(user)
        return Response({"message": f"User {user.username} removed from contributors"}, status=200)

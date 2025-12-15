from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, extend_schema_view
from drf_spectacular.types import OpenApiTypes
from .models import User
from .permissions import IsUserSelf
from user.serializers import UserSerializer


@extend_schema(tags=["User"])
class SignupView(CreateAPIView):
    """
    Represents a view for handling user signup operations.
    <br>
    <br>This view allows the creation of new user accounts in API.
    <br>**Authentification required**: No
    <br>**Permissions required**: None
    <br>Returns a `201 Created` response code on success.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    get=extend_schema(
        summary="Récupérer son profil utilisateur",
        description="Permet à un utilisateur authentifié de consulter son propre profil.",
        tags=["User"],
    ),
    put=extend_schema(
        summary="Mettre à jour complètement son profil",
        description="Remplace toutes les données du profil (tous les champs requis doivent être fournis).",
        tags=["User"],
    ),
    patch=extend_schema(
        summary="Mettre à jour partiellement son profil",
        description="Permet à un utilisateur de modifier ses informations personnelles.",
        tags=["User"],
        examples=[
            OpenApiExample(
                "Mise à jour partielle",
                description="Exemple de modification de quelques champs",
                value={
                    "first_name": "Jean-Pierre",
                    "age": 26,
                },
                request_only=True,
            ),
        ],
    ),
    delete=extend_schema(
        summary="Supprimer son compte",
        description="Permet à un utilisateur de supprimer définitivement son compte. Action irréversible.",
        tags=["User"],
    ),
)
class UserProfileView(RetrieveUpdateDestroyAPIView):
    """
    Represents the user profile view for interacting with authenticated user data.

    Provides endpoints for retrieving, updating, and deleting an authenticated user's
    profile. This includes complete or partial updates of profile data, and the
    deletion of the account is irreversible.

    :ivar queryset: Represents the collection of user objects available for querying.
    :type queryset: QuerySet

    :ivar serializer_class: Specifies the serializer used for transforming user data
        to and from JSON.
    :type serializer_class: Serializer

    :ivar permission_classes: Defines the list of permissions required to access
        this endpoint. Ensures the user is authenticated and operates on their
        own profile.
    :type permission_classes: list
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserSelf]

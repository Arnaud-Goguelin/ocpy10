from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .permissions import IsUserSelf
from .serializers import UserSerializer


class SignupView(CreateAPIView):
    """
    Handles the signup process by providing an API view for user creation.
    This is a public view, no authentication is required.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserProfileView(RetrieveUpdateDestroyAPIView):
    """
    Handles user profile operations including get, update, and deletion.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserSelf]

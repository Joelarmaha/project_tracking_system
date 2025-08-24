from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()


# Register new users
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]   # allow signup without login


# List all users (optional, for testing/admin only)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




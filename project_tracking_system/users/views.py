from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from .serializers import UserSerializer


# Register endpoint
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# User list (optional)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Full CRUD for users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def users_root(request):
    return JsonResponse({
        "register": "/api/users/register/",
        "login": "/api/users/login/",
        "token_refresh": "/api/users/token/refresh/"
    })



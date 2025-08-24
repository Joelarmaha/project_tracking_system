from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView
from users.views import UserRegisterView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("register/", RegisterView.as_view(), name="user-register"),
    path("users/", UserListView.as_view(), name="user-list"),
]


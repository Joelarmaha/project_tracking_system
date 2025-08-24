from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """For reading user data (profile, list, etc.)"""
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff"]
        read_only_fields = ["id", "is_staff"]


class UserRegisterSerializer(serializers.ModelSerializer):
    """For registering new users"""
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        # Ensure password is hashed
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user

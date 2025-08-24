from rest_framework import serializers
from .models import Project
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["id", "project", "created_at", "updated_at"]


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "owner", "tasks", "created_at", "updated_at"]
        read_only_fields = ["id", "owner", "created_at", "updated_at"]


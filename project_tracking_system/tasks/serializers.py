from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Task
from datetime import datetime

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source="project.id")

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "status",
            "due_date", "priority", "project",
            "created_at", "updated_at"
        ]
        read_only_fields = ["id", "project", "created_at", "updated_at"]

    def validate_due_date(self, value):
        now = timezone.now()
        if value < now:
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def update(self, instance, validated_data):
        if instance.status == "completed":
            raise serializers.ValidationError(
                "Completed tasks cannot be edited. Revert to 'In Progress' first."
            )
        return super().update(instance, validated_data)


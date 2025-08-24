from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="project.owner.username")

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "status",
            "due_date", "priority", "project",
            "owner", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "owner", "created_at", "updated_at"]

    def validate_due_date(self, value):
        if value and value <= timezone.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        return value

    def update(self, instance, validated_data):
        # Example: prevent editing completed tasks
        if instance.status == "completed":
            raise serializers.ValidationError(
                "Completed tasks cannot be edited. Revert to 'In Progress' first."
            )
        return super().update(instance, validated_data)



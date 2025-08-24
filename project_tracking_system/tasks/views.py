from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from projects.models import Project
from rest_framework.exceptions import PermissionDenied


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        return Task.objects.filter(project__id=project_id, project__owner=self.request.user)

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_pk")
        project = Project.objects.get(id=project_id)

        if project.owner != self.request.user:
            raise PermissionDenied("You do not have permission to add tasks to this project.")

        serializer.save(project=project)

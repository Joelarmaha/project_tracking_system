from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwnerOrReadOnly
from django.shortcuts import render


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectOwnerOrReadOnly]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def projects_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, "projects/projects_list.html", {"projects": projects})




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import ProjectViewSet, projects_list
from tasks.views import TaskViewSet

# Main router for projects
router = DefaultRouter()
router.register(r'', ProjectViewSet, basename="projects")   # note: '' instead of 'projects'

# Nested router for tasks inside projects
projects_router = routers.NestedDefaultRouter(router, r'', lookup='project')
projects_router.register(r'tasks', TaskViewSet, basename="project-tasks")

urlpatterns = [
    path("", include(router.urls)),                      # /api/projects/
    path("", include(projects_router.urls)),             # /api/projects/{id}/tasks/
    path("list/", projects_list, name="projects_list"),  # /api/projects/list/
]

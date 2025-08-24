from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from tasks.views import TaskViewSet
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename="projects")

# Nested router for tasks inside projects
projects_router = routers.NestedDefaultRouter(router, r'projects', lookup='project')
projects_router.register(r'tasks', TaskViewSet, basename="project-tasks")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(projects_router.urls)),
]

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from projects.models import Project
from tasks.models import Task


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_root(request, format = None):
    return Response({
        "users": "/api/users/",
        "projects": "/api/projects/",
        "tasks": "/api/tasks/"
    })


def dashboard_page(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    tasks_completed = Task.objects.filter(status="completed").count()
    return render(request, "dashboard.html", {
        "projects": projects,
        "tasks": tasks,
        "tasks_completed": tasks_completed,
    })


def register_page(request):
    return render(request, "register.html")


def login_page(request):
    return render(request, "login.html")


def password_reset(request):
    return render(request, "password_reset.html")


def logout_view(request):
    logout(request)
    return redirect("login_page")


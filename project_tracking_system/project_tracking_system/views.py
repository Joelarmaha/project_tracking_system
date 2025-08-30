from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


@api_view(["GET"])
@permission_classes([IsAuthenticated])   # 👈 must be inside a list
def api_root(request, format=None):
    return Response({
        "users": "/api/users/",
        "projects": "/api/projects/",
        "tasks": "/api/tasks/"
    })


def register_page(request):
    return render(request, "register.html")
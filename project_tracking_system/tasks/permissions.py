from rest_framework import permissions


class IsTaskOwnerOrAssignee(permissions.BasePermission):
    """
    Custom permission: Only project owner or task assignee can edit the task.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.project.owner == request.user or obj.assigned_to == request.user


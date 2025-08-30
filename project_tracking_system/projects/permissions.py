from rest_framework import permissions


class IsProjectOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only project owner can edit/delete.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


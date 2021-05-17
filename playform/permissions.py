from rest_framework.permissions import BasePermission

class UserOwnershipPermission(BasePermission):
    """
    Handles user ownership.
    Confirms resource `owner` matches request user.
    """

    def has_object_permission(self, request, view, obj):
        """Compares request user against object owner"""
        return request.user == obj.owner
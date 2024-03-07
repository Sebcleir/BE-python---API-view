from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST" and request.user.is_superuser:
            return True
        elif request.method == "GET":
            return True

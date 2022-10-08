from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import BlockUser


class BlocklistPermission(BasePermission):
    """
    Global permission check for blocked users
    """

    def has_permission(self, request, view):
        blocked = BlockUser.objects.filter(username=request.user.username).exists()
        return not blocked


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user
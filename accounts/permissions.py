from rest_framework import permissions
from accounts.models import UserRoleChoices


class IsSalesGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.role == UserRoleChoices.SALES
            )
        )


class IsSupportGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.role == UserRoleChoices.SUPPORT
            )
        )


class IsManagementGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.role == UserRoleChoices.MANAGEMENT
            )
        )

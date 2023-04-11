from rest_framework import permissions
from accounts.models import UserRoleChoices


class IsSalesGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.group == UserRoleChoices.SALES[0]
            )
        )


class IsSupportGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.group == UserRoleChoices.SUPPORT[0]
            )
        )


class IsManagementGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.group == UserRoleChoices.MANAGEMENT[0]
            )
        )

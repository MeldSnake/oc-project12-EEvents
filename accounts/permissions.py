from django.utils.translation import gettext_lazy as _
from rest_framework import permissions

from accounts.models import UserRoleChoices


class IsSalesGroup(permissions.BasePermission):
    message = _("You are not a member of the Sales team")

    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.role == UserRoleChoices.SALES
            )
        )


class IsSupportGroup(permissions.BasePermission):
    message = _("You are not a member of the Support team")

    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.role == UserRoleChoices.SUPPORT
            )
        )


class IsManagementGroup(permissions.BasePermission):
    message = _("You are not a member of the Management team")

    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_staff
                or request.user.role == UserRoleChoices.MANAGEMENT
            )
        )

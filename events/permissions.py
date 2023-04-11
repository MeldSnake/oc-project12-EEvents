from typing import TYPE_CHECKING

from rest_framework import permissions

from accounts.models import UserRoleChoices

if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.views import View

    from accounts.models import User

    from .models import Event


class IsEventContact(permissions.BasePermission):
    def has_object_permission(
        self,
        request: "HttpRequest",
        view: "View",
        obj: "Event",
    ):
        if request.user.is_staff:
            return True
        user: "User" = request.user  # type: ignore
        if user.role in [UserRoleChoices.MANAGEMENT, UserRoleChoices.ADMIN]:
            return True
        elif user.role == UserRoleChoices.SUPPORT:
            # Check event support_contact
            return obj.support_contact == user
        elif user.role == UserRoleChoices.SALES:
            # Check event client sales_contact
            return obj.contract.client.sales_contact
        return False

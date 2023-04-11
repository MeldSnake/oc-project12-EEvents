from typing import TYPE_CHECKING

from rest_framework import permissions

from accounts.models import UserRoleChoices

if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.views import View

    from .models import Client


class IsSalesContactOrManagement(permissions.BasePermission):
    def has_object_permission(
        self,
        request: "HttpRequest",
        view: "View",
        obj: "Client",
    ):
        if request.user.is_staff:
            return True
        return (
            request.user.role == UserRoleChoices.MANAGEMENT  # type: ignore
            or request.user == obj.sales_contact
        )

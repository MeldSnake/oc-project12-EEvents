from typing import TYPE_CHECKING

from django.utils.translation import gettext_lazy as _
from rest_framework import permissions

from accounts.models import UserRoleChoices

if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.views import View

    from .models import Contract


class IsSalesContactOrManagement(permissions.BasePermission):
    message = _("You are neither a member of the Sales or Management team")

    def has_object_permission(
        self,
        request: "HttpRequest",
        view: "View",
        obj: "Contract",
    ):
        if request.user.is_staff:
            return True
        return (
            request.user.role == UserRoleChoices.MANAGEMENT  # type: ignore
            or request.user == obj.client.sales_contact
        )

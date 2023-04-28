"""epicevents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.models import User, UserRoleChoices


def exception_view(request):
    """Exception route to test sentry connexion"""
    dzero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("accounts.urls")),
    path("clients/", include("clients.urls")),
    path("contracts/", include("contracts.urls")),
    path("events/", include("events.urls")),
    path(
        "token/",
        view=TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        view=TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    # path("sentry_test/", exception_view),
]


def create_user_groups():
    """Ensure that the default groups are present"""
    try:
        # obtaining all permissions per model
        user_perms = Permission.objects.filter(
            content_type__app_label="accounts",
            content_type__model="user",
        )
        client_perms = Permission.objects.filter(
            content_type__app_label="clients",
            content_type__model="client",
        )
        contract_perms = Permission.objects.filter(
            content_type__app_label="contracts",
            content_type__model="contract",
        )
        event_perms = Permission.objects.filter(
            content_type__app_label="events",
            content_type__model="event",
        )

        # Creating or Obtaining the group management
        (
            management_group,
            created,
        ) = Group.objects.get_or_create(name="management")
        for permission in [*user_perms, *client_perms, *contract_perms, *event_perms]:
            management_group.permissions.add(permission)

        # Creating or Obtaining the group sales
        (
            sales_group,
            created,
        ) = Group.objects.get_or_create(name="sales")
        permissions = [
            *user_perms.filter(
                codename__in=[
                    "view_user",
                ],
            ),
            *client_perms.filter(
                codename__in=[
                    "add_client",
                    "view_client",
                    "change_client",
                ],
            ),
            *contract_perms.filter(
                codename__in=[
                    "add_contract",
                    "view_contract",
                    "change_contract",
                ],
            ),
            *event_perms.filter(
                codename__in=[
                    "add_event",
                    "view_event",
                ],
            ),
        ]
        for permission in permissions:
            sales_group.permissions.add(permission)

        # Creating or Obtaining the group support
        (
            support_group,
            created,
        ) = Group.objects.get_or_create(name="support")
        permissions = [
            *client_perms.filter(
                codename__in=[
                    "view_client",
                ],
            ),
            *user_perms.filter(
                codename__in=[
                    "view_user",
                ],
            ),
            *contract_perms.filter(
                codename__in=[
                    "view_contract",
                ],
            ),
            *event_perms.filter(
                codename__in=[
                    "view_event",
                    "change_event",
                ],
            ),
        ]
        for permission in permissions:
            support_group.permissions.add(permission)

        for user in User.objects.all():
            if user.role == UserRoleChoices.SALES:
                user.groups.add(sales_group)
            elif user.role == UserRoleChoices.SUPPORT:
                user.groups.add(support_group)
            elif user.role == UserRoleChoices.MANAGEMENT:
                user.groups.add(management_group)
            # elif user.role == UserRoleChoices.ADMIN:
            #     user.groups
    except Exception:  # Else this would throw right before migrations start
        pass


# Weird way to create groups after the migrations, would not work in migrations
# since the permissions are created after all migrations are executed.
create_user_groups()

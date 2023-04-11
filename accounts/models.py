from typing import Type

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class UserRoleChoices(models.TextChoices):
    ADMIN = "admin", _("Administrator")
    SALES = "sales", _("Sales")
    SUPPORT = "support", _("Support")
    MANAGEMENT = "management", _("Management")


class User(AbstractUser):
    role = models.CharField(
        _("User role"),
        choices=UserRoleChoices.choices,
        max_length=10,
    )


def unassign_user_role_group(user: User, role: UserRoleChoices):
    match role:
        case UserRoleChoices.SALES:
            group = Group.objects.get(name="sales")
        case UserRoleChoices.SUPPORT:
            group = Group.objects.get(name="support")
        case UserRoleChoices.MANAGEMENT:
            group = Group.objects.get(name="management")
        case _:
            group = None
    user.groups.remove(group)


def assign_user_role_group(user: User, *, role: UserRoleChoices | None = None):
    match (role or user.role):
        case UserRoleChoices.SALES:
            group = Group.objects.get(name="sales")
        case UserRoleChoices.SUPPORT:
            group = Group.objects.get(name="support")
        case UserRoleChoices.MANAGEMENT:
            group = Group.objects.get(name="management")
        case _:
            group = None
    user.groups.add(group)


@receiver(post_save, sender=User)
def user_post_save_receiver(
    sender: Type[User],
    instance: User,
    created: bool,
    raw: bool,
    using: str,
    update_fields: list[str] | None,
    **kwargs,
):
    if raw:
        return
    update_fields = update_fields or []
    if "role" in update_fields or created:
        assign_user_role_group(instance, role=instance.role)  # type: ignore
    if "is_staff" in update_fields or created:
        if instance.is_staff:
            assign_user_role_group(instance, role=UserRoleChoices.ADMIN)


@receiver(pre_save, sender=User)
def user_pre_save_receiver(
    sender: Type[User],
    instance: User,
    raw: bool,
    using: str,
    update_fields: list[str] | None,
    **kwargs,
):
    if raw:
        return
    update_fields = update_fields or []
    if "role" in update_fields:
        unassign_user_role_group(instance, role=instance.role)  # type: ignore
    if "is_staff" in update_fields:
        if instance.is_staff:
            unassign_user_role_group(instance, UserRoleChoices.ADMIN)

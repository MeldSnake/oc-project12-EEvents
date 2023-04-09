from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class UserRoleChoices(models.TextChoices):
    ADMIN = "admin", _("Administrator")
    SALES = "sales", _("Sales")
    SUPPORT = "support", _("Support")


class User(AbstractUser):

    role = models.CharField(
        _("User role"),
        choices=UserRoleChoices.choices,
        max_length=10,
    )

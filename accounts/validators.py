from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User, UserRoleChoices


def validate_sales_user(user_pk: int):
    user = User.objects.get(pk=user_pk)
    if not user.role == UserRoleChoices.SALES:
        raise ValidationError(
            _("The user is not part of the sale group"),
            params={'user': user}
        )


def validate_support_user(user_pk: int):
    user = User.objects.get(pk=user_pk)
    if not user.role == UserRoleChoices.SUPPORT:
        raise ValidationError(
            _("The user is not part of the support group"),
            params={'user': user}
        )
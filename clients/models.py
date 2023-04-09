from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from accounts.validators import validate_sales_user


class Client(models.Model):
    first_name = models.CharField(
        _("First Name"),
        max_length=25,
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=25,
    )
    company_name = models.CharField(
        _("Company Name"),
        max_length=250,
        unique=True,
    )
    email = models.EmailField(
        _("Email"),
        max_length=254,
        null=True,
    )
    phone = PhoneNumberField(
        _("Phone line"),
        null=True,
        blank=True,
    )
    mobile = PhoneNumberField(
        _("Mobile"),
        null=True,
        blank=True,
    )
    date_creation = models.DateTimeField(
        _("Date creation"),
        auto_now=False,
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        _("Date last updated"),
        auto_now=True,
    )
    status = models.BooleanField(
        _("Is active client"),
        default=False,
    )
    sales_contact = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Sales contact"),
        on_delete=models.SET_NULL,
        validators=[validate_sales_user],
        null=True,
        related_name="clients",
    )

    # facebook = models.CharField(_("Facebook"), max_length=50)
    # twitter = models.CharField(_("Twitter"), max_length=50)
    # linkedin = models.CharField(_("LinkedIn"), max_length=50)

    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("clients")
        get_latest_by = ["date_creation", "date_updated"]
        indexes = [
            models.Index(fields=["company_name"], name="company_name_idx"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} @ {self.company_name}"

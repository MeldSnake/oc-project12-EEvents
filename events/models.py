from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from accounts.validators import validate_support_user


class EventStatusChoices(models.TextChoices):
    FINANCED = "financed", _("Financed")
    PLANNED = "planned", _("Planned")
    PENDING = "pending", _("Pending")
    COMPLETED = "completed", _("Completed")


class Event(models.Model):

    date_creation = models.DateTimeField(
        _("Date creation"),
        auto_now=False,
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        _("Date last updated"),
        auto_now=True,
    )
    event_status = models.CharField(
        _("Event status"),
        choices=EventStatusChoices.choices,
        default=EventStatusChoices.FINANCED[0],
        max_length=15,
    )
    attendees = models.IntegerField(_("Attendees"))
    event_date = models.DateField(
        _("Event date"),
        auto_now=False,
        auto_now_add=False,
        null=True,
    )
    notes = models.TextField(
        verbose_name=_("Notes"),
        null=True,
        blank=True,
    )
    support_contact = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Support contact"),
        on_delete=models.SET_NULL,
        validators=[validate_support_user],
        null=True,
        blank=True,
        related_name="events",
    )
    contract = models.OneToOneField(
        "contracts.Contract",
        verbose_name=_("Event"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=None,
        related_name="event",
    )

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

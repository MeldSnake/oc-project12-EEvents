from typing import Type
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils import formats
from django.utils.translation import gettext_lazy as _
from accounts.validators import validate_support_user
from accounts.models import UserRoleChoices


class EventStatusChoices(models.TextChoices):
    FINANCED = "financed", _("Financed")
    PLANNED = "planned", _("Planned")
    PENDING = "pending", _("Pending")
    COMPLETED = "completed", _("Completed")


class EventStatus(models.Model):
    name = models.CharField(
        _("Status name"),
        unique=True,
    )

    class Meta:
        verbose_name = _("event status")
        verbose_name_plural = _("event statuses")

    def __str__(self):
        return self.name.capitalize()


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
    event_status = models.ForeignKey(
        EventStatus,
        models.SET_NULL,
        null=True,
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
        null=True,
        blank=True,
        related_name="events",
        limit_choices_to=models.Q(
            role__in=[
                UserRoleChoices.SUPPORT,
            ],
        ),
    )
    contract = models.OneToOneField(
        "contracts.Contract",
        verbose_name=_("Contract"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=None,
        related_name="event",
        limit_choices_to=models.Q(
            event=None,
        ),
    )

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return f"{str(self.contract.client)} -> {formats.date_format(self.event_date, 'SHORT_DATE_FORMAT')}"


@receiver(pre_save, sender=Event)
def event_pre_save_receiver(
    sender: Type[Event],
    instance: Event,
    raw: bool,
    using: str,
    update_fields: list[str] | None,
    **kwargs,
):
    if instance.support_contact is not None:
        validate_support_user(instance.support_contact)

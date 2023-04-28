from typing import Type
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from clients.models import Client


class Contract(models.Model):
    date_creation = models.DateTimeField(
        _("Date creation"),
        auto_now=False,
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        _("Date last updated"),
        auto_now=True,
    )
    amount = models.FloatField(_("Price"))
    payment_due = models.DateTimeField(
        _("Payment due"),
        auto_now=False,
        auto_now_add=False,
    )
    client = models.ForeignKey(
        "clients.Client",
        verbose_name=_("Client"),
        on_delete=models.CASCADE,
        related_name="contracts",
    )

    class Meta:
        verbose_name = _("contract")
        verbose_name_plural = _("contracts")

    def __str__(self):
        return f"{str(self.client)} - Contract {self.pk}"


@receiver(post_save, sender=Contract)
def update_client_status_on_contract(
    sender: Type[Contract],
    instance: Contract,
    created: bool,
    raw: bool,
    using: str,
    update_fields: list[str] | None,
    **kwargs,
):
    if raw or instance is None:
        return
    update_fields = update_fields or []
    client: Client = instance.client
    if "status" in update_fields or (created and instance.client):
        if not client.status:
            client.status = True
            client.save()

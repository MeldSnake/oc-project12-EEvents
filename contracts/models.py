from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


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

    def get_absolute_url(self):
        return reverse("contract_detail", kwargs={"pk": self.pk})

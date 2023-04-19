from django.db import models
from django_filters import rest_framework as filters

from clients.models import Client
from extras.filters import CustomDateFilter


def contract_clients(request):
    return Client.objects.filter(status=True)


class ContractFilterSet(filters.FilterSet):
    paid = filters.BooleanFilter(method="is_contract_paid_filter")
    # MAYBE client filter (by name/mail/company?)
    client = filters.ModelChoiceFilter(queryset=contract_clients)
    payment_date = CustomDateFilter(field_name="payment_due")
    payment = filters.DateFromToRangeFilter(field_name="payment_due")

    class Meta:
        fields = [
            "paid",
            "client",
            "payment_date",
            "payment",
        ]

    def is_contract_paid_filter(
        self,
        queryset: models.QuerySet,
        name: str,
        value: bool,
    ):
        return queryset.filter(**{"event__isnull": not value})

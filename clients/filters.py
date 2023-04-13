from django_filters import rest_framework as filters


class ClientFilterSet(filters.FilterSet):
    active = filters.BooleanFilter(field_name="status")
    no_contact = filters.BooleanFilter(field_name="sales_contact", lookup_expr="isnull")
    email = filters.CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        fields = [
            "active",
            "no_contact",
            "email",
        ]

from django_filters import rest_framework as filters

from extras.filters import CustomDateFilter


class EventFilterSet(filters.FilterSet):
    status = filters.CharFilter(method='status_filter')
    attendees = filters.RangeFilter()
    event_date_at = CustomDateFilter(field_name="event_date")
    event_date = filters.DateFromToRangeFilter()
    no_contact = filters.BooleanFilter(
        field_name="support_contact",
        lookup_expr="isnull",
    )

    class Meta:
        fields = [
            # 'status',
            "attendees",
            "event_date_at",
            "event_date",
            "no_contact",
        ]

    def status_filter(self, queryset, fieldname, value):
        return queryset.filter(
            event_status__name=value,
        )

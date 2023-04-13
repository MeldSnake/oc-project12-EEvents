import datetime

from django import forms
from django_filters import rest_framework as filters


class CustomDateFilter(filters.Filter):
    """
    Filter supporting validation against datetime values
    """

    field_class = forms.DateField

    def filter(self, qs, value):
        if value:
            # Convert a datetime to a date if required
            if isinstance(value, datetime.datetime):
                value = value.date()
            # Create the start/end of day datetime values
            start_value = forms.utils.from_current_timezone(
                datetime.datetime.combine(value, datetime.time.min)
            )
            end_value = forms.utils.from_current_timezone(
                datetime.datetime.combine(value, datetime.time.max)
            )
            # Create the filter
            return self.get_method(qs)(
                **{
                    f"{self.field_name}__gte": start_value,
                    f"{self.field_name}__lte": end_value,
                }
            )
        return qs

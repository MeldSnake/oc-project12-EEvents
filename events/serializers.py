from rest_framework import serializers
from .models import Event, EventStatus


class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    event_status = serializers.SlugRelatedField(
        slug_field="name",
        queryset=EventStatus.objects.all(),
    )

    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {
            'date_creation': {
                'read_only': True,
            },
            'date_updated': {
                'read_only': True,
            },
        }

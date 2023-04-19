from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
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

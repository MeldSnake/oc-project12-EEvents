from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        extra_kwargs = {
            'date_creation': {
                'read_only': True,
            },
            'date_updated': {
                'read_only': True,
            },
        }

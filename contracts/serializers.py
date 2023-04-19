from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        extra_kwargs = {
            'date_creation': {
                'read_only': True,
            },
            'date_updated': {
                'read_only': True,
            },
        }

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from .filters import EventFilterSet
from .models import Event
from .permissions import IsEventContact
from .serializers import EventSerializer


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permissions = [
        permissions.DjangoModelPermissions,
    ]
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = EventFilterSet

    # TODO Add paging system for list


class EventAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        permission_classes = [
            permissions.DjangoModelPermissions(),
        ]
        if self.request.method in ["PUT", "PATCH"]:
            permission_classes.append(IsEventContact())
        return permission_classes

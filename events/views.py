from rest_framework import permissions, generics
from .models import Event
from .serializers import EventSerializer


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permissions = [
        permissions.DjangoModelPermissions,
    ]
    # TODO Add paging system for list


class EventAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    # TODO Can anyone access from id or shall only assigned contacts be allowed

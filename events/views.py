from rest_framework import generics
from .models import Event
from .serializers import EventSerializer


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # TODO Add paging system for list

    # TODO Permissions create/list for sales only
    # TODO All permissions for admin


class EventAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # TODO Can anyone access from id or shall only assigned contacts be allowed

    # TODO Permission retrieve for sales/support
    # TODO Permission update for support only
    # TODO Can the sales also update the values of the event
    # TODO All permissions for admin

from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer


class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # TODO Add paging system

    # TODO Permissions create/list for sales only
    # TODO All permissions for admin


class ClientAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # TODO Can anyone access from id or shall only assigned contacts be allowed

    # TODO Permission retrieve for sales/support
    # TODO Permission update for sales only
    # TODO All permissions for admin

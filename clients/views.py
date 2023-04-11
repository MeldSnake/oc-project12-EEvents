from rest_framework import generics, permissions
from .models import Client
from .serializers import ClientSerializer


class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    # TODO Add paging system


class ClientAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    # TODO Can support modify a client ?
    # TODO Contacts only shall be allowed to modify ?

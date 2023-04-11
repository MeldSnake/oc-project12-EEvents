from rest_framework import generics, permissions
from .models import Client
from .serializers import ClientSerializer
from .permissions import IsSalesContactOrManagement


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

    def get_permissions(self):
        permission_classes = [
            permissions.DjangoModelPermissions(),
        ]
        if self.request.method in ["PUT", "PATCH"]:
            permission_classes.append(IsSalesContactOrManagement())
        return permission_classes

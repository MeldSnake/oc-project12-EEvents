from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions

from .filters import ClientFilterSet
from .models import Client
from .permissions import IsSalesContactOrManagement
from .serializers import ClientSerializer


class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        "first_name",
        "last_name",
        "company_name",
    ]
    filterset_class = ClientFilterSet

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

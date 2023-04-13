from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from .filters import ContractFilterSet
from .models import Contract
from .permissions import IsSalesContactOrManagement
from .serializers import ContractSerializer


class ContractListCreate(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = ContractFilterSet

    # TODO Add paging system for list


class ContractAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def get_permissions(self):
        permission_classes = [
            permissions.DjangoModelPermissions(),
        ]
        if self.request.method in ["PUT", "PATCH"]:
            permission_classes.append(IsSalesContactOrManagement())
        return permission_classes

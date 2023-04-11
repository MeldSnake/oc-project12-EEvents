from rest_framework import generics, permissions
from .models import Contract
from .serializers import ContractSerializer


class ContractListCreate(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    # TODO Add paging system for list


class ContractAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    # TODO Can anyone access from id or shall only assigned contacts be allowed

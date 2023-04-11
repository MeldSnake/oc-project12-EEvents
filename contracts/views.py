from rest_framework import generics, permissions
from .models import Contract
from .serializers import ContractSerializer
from .permissions import IsSalesContactOrManagement


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

    def get_permissions(self):
        permission_classes = [
            permissions.DjangoModelPermissions(),
        ]
        if self.request.method in ["PUT", "PATCH"]:
            permission_classes.append(IsSalesContactOrManagement())
        return permission_classes

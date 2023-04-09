from rest_framework import generics
from .models import Contract
from .serializers import ContractSerializer


class ContractListCreate(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # TODO Add paging system for list

    # TODO Permissions create/list for sales only
    # TODO All permissions for admin


class ContractAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # TODO Can anyone access from id or shall only assigned contacts be allowed

    # TODO Permission retrieve for sales/support
    # TODO Permission update for support only
    # TODO All permissions for admin

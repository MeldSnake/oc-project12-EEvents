from rest_framework import generics
from .models import Contract
from .serializers import ContractSerializer


class ContractListCreate(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

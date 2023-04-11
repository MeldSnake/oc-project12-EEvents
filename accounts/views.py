from rest_framework import generics, permissions

from .models import User
from .serializers import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]
    # TODO Add paging system for list


class UserAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
    ]

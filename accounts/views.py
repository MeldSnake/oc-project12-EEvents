from rest_framework import generics, permissions

from .models import User
from .serializers import UserSerializer


# TODO The management team shall be able to create users
# (not up to management team since this would be a security issue)
# Admin can create any kind of account though


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
        permissions.IsAdminUser,
    ]
    # TODO Add paging system for list


class UserAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
        permissions.IsAdminUser,
    ]

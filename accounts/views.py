from rest_framework import generics, permissions

from .models import User, UserRoleChoices
from .serializers import UserSerializer
from .permissions import IsManagementGroup


# TODO The management team shall be able to create users
# (not up to management team since this would be a security issue)
# Admin can create any kind of account though


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = [
            permissions.DjangoModelPermissions(),
            permissions.IsAuthenticated(),
        ]
        if self.request.method == "POST":
            permission_classes.append(IsManagementGroup())
        return permission_classes

    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        return (
            super()
            .get_queryset()
            .exclude(
                role=UserRoleChoices.ADMIN,
            )
        )

    # TODO Add paging system for list


class UserAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
        permissions.IsAuthenticated,
    ]

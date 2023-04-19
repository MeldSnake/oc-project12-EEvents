from rest_framework import generics, permissions, exceptions
from django.utils.translation import gettext_lazy as _

from .models import User, UserRoleChoices
from .serializers import UserSerializer
from .permissions import IsManagementGroup


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if self.request.user.role != UserRoleChoices.ADMIN:
            role = serializer.validated_data.get('role')
            if role in [UserRoleChoices.ADMIN, UserRoleChoices.MANAGEMENT]:
                raise exceptions.PermissionDenied(
                    _("Only an administrator can create a user with this role")
                )
        return super().perform_create(serializer)

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


class UserAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.DjangoModelPermissions,
        permissions.IsAuthenticated,
    ]

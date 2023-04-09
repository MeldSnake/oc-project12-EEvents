from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO Add paging system for list

    # TODO Permissions create/list for sales only
    # TODO All permissions for admin


class UserAccess(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO Can anyone access from id or shall only assigned contacts be allowed

    # TODO Permission retrieve for sales/support
    # TODO Permission update for support only
    # TODO Can the sales also update the values of the event
    # TODO All permissions for admin

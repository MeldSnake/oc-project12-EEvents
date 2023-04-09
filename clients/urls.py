from django.urls import path
from .views import (
    ClientListCreate,
    ClientAccess,
)

urlpatterns = [
    path("", view=ClientListCreate.as_view(), name="client_list"),
    path("<int:pk>", view=ClientAccess.as_view(), name="client_detail"),
]

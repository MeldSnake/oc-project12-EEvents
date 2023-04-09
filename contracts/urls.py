from django.urls import path
from .views import (
    ContractListCreate,
    ContractAccess,
)

urlpatterns = [
    path("", view=ContractListCreate.as_view(), name="contract_list"),
    path("<int:pk>", view=ContractAccess.as_view(), name="contract_detail"),
]

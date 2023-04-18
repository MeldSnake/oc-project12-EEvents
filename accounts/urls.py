from django.urls import path
from .views import (
    UserListCreate,
    UserAccess,
)

urlpatterns = [
    path("", view=UserListCreate.as_view(), name="user_list"),
    path("<int:pk>/", view=UserAccess.as_view(), name="user_detail"),
]

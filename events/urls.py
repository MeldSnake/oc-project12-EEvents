from django.urls import path, re_path
from .views import (
    EventListCreate,
    EventAccess,
)

urlpatterns = [
    path("", view=EventListCreate.as_view(), name="event_list"),
    path("<int:pk>/", view=EventAccess.as_view(), name="event_detail"),
]

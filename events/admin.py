from django.contrib import admin
from .models import Event, EventStatus

admin.site.register(Event)
admin.site.register(EventStatus)

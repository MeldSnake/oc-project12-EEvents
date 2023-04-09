from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["username", "email", "role"]

    def get_fieldsets(self, request, obj):
        # -> List[Tuple[Optional[str], Dict[str, Any]]]:
        return (
            *super().get_fieldsets(request, obj),
            (
                "EpicEvent",
                {
                    "fields": ("role",),
                },
            ),
        )


admin.site.register(User, UserAdmin)

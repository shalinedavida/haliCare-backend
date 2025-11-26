from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["date_joined"]
    list_display = [
        "phone_number",
        "first_name",
        "last_name",
        "user_type",
        "is_active",
        "is_staff",
    ]
    search_fields = ["phone_number", "first_name", "last_name"]
    list_filter = ["user_type", "is_active", "is_staff"]

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "user_type")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "first_name",
                    "last_name",
                    "user_type",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)

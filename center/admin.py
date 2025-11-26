from django.contrib import admin
from .models import Center

# Register your models here.


class CenterAdmin(admin.ModelAdmin):
    list_display = ("center_name", "center_type", "address", "operational_status")
    list_filter = ("center_type",)


admin.site.register(Center, CenterAdmin)

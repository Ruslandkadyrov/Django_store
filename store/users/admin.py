from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "contact_number"]
    list_editable = ["contact_number"]
    search_fields = ["first_name", "last_name", "contact_number"]


admin.site.register(CustomUser, CustomUserAdmin)

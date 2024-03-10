from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "contact_number", "town", "adress"]


admin.site.register(CustomUser, CustomUserAdmin)

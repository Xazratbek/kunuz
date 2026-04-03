from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["id","email","username","first_name","last_name","age","is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (None,{"fields": ("age",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{"fields": ('age',)}),
    )

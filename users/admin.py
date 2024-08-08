from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserAccount
from .forms import CustomUserChangeForm,CustomUserCreationForm
# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering =["email"]
    list_display=['email','last_name', 'first_name','is_staff','is_active']
    list_display_links=["email"]
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=UserAccount
    list_filter=['email','last_name', 'first_name','is_staff','is_active']
    fieldsets = (
        (
            _("Login Credentials"), {
                "fields": ("email", "password",)
            }, 
        ),
        (
            _("Personal Information"),
            {
                "fields": ('first_name', 'last_name',)
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login",)
            },
        ),
    )
    add_fieldsets = (
            (None, {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
            },),
        )
    search_fields=['email','last_name', 'first_name']

admin.site.register(UserAccount,UserAdmin)
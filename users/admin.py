from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DefaultUserConfig
from django.utils.translation import gettext_lazy as _

from users.models import UserTag

@admin.register(get_user_model())
class UserAdmin(DefaultUserConfig):
    model = get_user_model()
    readonly_fields = ('date_joined',)
    ordering = ('email',)

    filter_horizontal = ('groups', 'user_permissions')
    list_display = ('email', 'handle', 'first_name', 'last_name', 'date_joined')

    fieldsets = (
        (_('Credentials'), {
            'fields': ('email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('handle', 'first_name', 'last_name', 'description', 'avatar',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions')
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

@admin.register(UserTag)
class UserTag(admin.ModelAdmin):
    model = UserTag
    readonly_fields = ('date_created',)

    list_display = ('tag', 'date_created')


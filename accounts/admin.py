from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

Account = get_user_model()


class UserAdmin(UserAdmin):
    list_display = ('email',)
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name',)}),
        ('Permissions', {'fields': ('user_permissions','groups','is_active','is_superuser','is_staff',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Account,UserAdmin)

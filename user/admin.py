from django.contrib import admin
from .models import (
    User,
    UserBanedIp,
)

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active',
                    'is_staff', 'is_moderator', 'created_at',
                    'updated_at', 'status_ban',)
    list_display_links = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    list_editable = (
        'is_active', 'is_staff', 'is_moderator',
        'status_ban'
    )
    list_filter = (
        'is_active', 'is_staff', 'is_moderator',
        'status_ban'
    )
    fields = (
        'username', 'email', 'is_active',
        'is_staff', 'is_moderator', 'avatar', 'password',
        'time_ban', 'status_ban',
    )


class UserBanedIpAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'ip_address', 'attempts', 'time_unblock',
        'status',
    )
    list_display_links = ('id', 'ip_address',)
    search_fields = ('id', 'ip_address',)
    list_editable = (
        'status',
    )
    list_filter = (
        'status',
    )
    fields = (
        'ip_address', 'attempts', 'time_unblock',
        'status',
    )


admin.site.register(User, UsersAdmin)
admin.site.register(UserBanedIp, UserBanedIpAdmin)
admin.site.site_title = 'Управление пользователями'
admin.site.site_header = 'Управление пользователями'

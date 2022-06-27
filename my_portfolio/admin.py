from django.contrib import admin
from .models import (
    PortfolioProject,
)


class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'created_at',
        'updated_at', 'is_public',
        'photo', 'link_project',
    )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_public',)
    list_filter = ('is_public',)
    fields = (
        'title', 'description', 'content', 'photo',
        'is_public', 'created_at', 'updated_at',
        'link_project',
    )
    readonly_fields = ('created_at',
                       'updated_at',)


admin.site.register(PortfolioProject, PortfolioProjectAdmin)
admin.site.site_title = 'Управление портфолио'
admin.site.site_header = 'Управление портфолио'

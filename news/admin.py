from django.contrib import admin
from .models import (
    News,
    Category,
    NewsLikes,
    Comment,
    FavoriteUserNews,
)

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'created_at',
        'updated_at', 'is_public',
        'photo', 'category', 'owner', 'offer',
    )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'owner')
    list_editable = ('is_public', 'offer')
    list_filter = ('is_public', 'category', 'offer')
    fields = (
        'title', 'description', 'category', 'content', 'photo',
        'is_public', 'created_at', 'updated_at', 'owner', 'liked',
        'offer', 'favorite_news',
    )
    readonly_fields = ('created_at',
                       'updated_at',)


class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title',)
    list_display = ('id', 'title',)
    search_fields = ('id', 'title')
    list_filter = ('title',)


class NewsLikesAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'user', 'news')
    list_display = ('id', 'user', 'news')
    search_fields = ('id', 'user', 'news')
    fields = (
        'user', 'news', 'value',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'news',
        'created_data', 'status'
    )
    list_display_links = ('id', 'news', 'user')
    search_fields = ('id', 'user', 'news')
    list_editable = ('status',)
    list_filter = ('status',)
    fields = (
        'user', 'news', 'text', 'status',
    )
    readonly_fields = ('created_data',)


class FavoriteUserNewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'news', 'user',
    )
    list_display_links = ('id', 'news',)
    fields = (
        'news', 'user',
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(NewsLikes, NewsLikesAdmin)
admin.site.register(FavoriteUserNews, FavoriteUserNewsAdmin)
admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'

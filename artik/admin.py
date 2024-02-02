from django.contrib.admin.decorators import register
from django.contrib import admin

from .models import Article


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    # prepopulated_fields = {'slug': ('title',)}

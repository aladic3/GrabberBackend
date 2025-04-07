from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
from django.contrib import admin
from .models import Tag, BlogPost, Comment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "content"]


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass

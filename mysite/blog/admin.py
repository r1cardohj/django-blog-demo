from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish_dt', 'status']
    list_filter = ['status', 'created_dt', 'publish_dt', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish_dt'
    ordering = ['status', 'publish_dt']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created_dt', 'active']
    list_filter = ['active', 'created_dt', 'updated_dt']
    search_fields = ['name', 'email', 'body']
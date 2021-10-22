from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status']
  list_filter = ('status', 'created', 'publish', 'updated')
  search_fields = ('title', 'body')
  raw_id_fields = ('author',)
  ordering = ('status', 'publish')
  date_hierarchy = 'publish'
  prepopulated_fields = {'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'post', 'body', 'created', 'updated', 'active')
  list_filter = ('created', 'updated', 'active')
  search_fields = ('name', 'email', 'body')



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
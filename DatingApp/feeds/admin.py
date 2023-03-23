from django.contrib import admin
from .models import *
# Register your models here.

class UserPost(admin.ModelAdmin):
    model = Posts
    list_display = ['user']
    list_filter = ['user']
    search_fields =['caption']

admin.site.register(Posts,UserPost)

class UserComment(admin.ModelAdmin):
    model = Comment
    list_display=['user']
    list_filter = ['user']
    search_fields = ['comment_text']

admin.site.register(Comment,UserComment)
from django.contrib import admin
from .models import Post, Image

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content']
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
from django.contrib import admin
from blog.models import Author, Category, Post, Tag

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'experience', 'social_media_url']
    search_fields = ['username', 'email']
    ordering = ['username']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'pub_date', 'status']
    list_filter = ['status', 'category', 'author']
    search_fields = ['title', 'description']
    ordering = ['-pub_date']
    filter_horizontal = ['tags']

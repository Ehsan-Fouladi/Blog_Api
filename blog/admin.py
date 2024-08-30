from django.contrib import admin
from .models import category_list, blog


@admin.register(category_list)
class AdminCategory(admin.ModelAdmin):
    list_display = ["title",]
    list_filter = ["title",]
    search_fields = ["title",]
    list_per_page = 6


@admin.register(blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ["user", "title", "author", "created_at"]
    list_filter = ["title", "author"]
    search_fields = ["user", "title", "category"]
    list_per_page = 10

from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","parent"]
    ordering = ["-id",]
    search_fields = ["name"]
    list_filter = ["name"]
    list_per_page = 20

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","slug","category","author","status","created_at"]
    prepopulated_fields = {"slug": ('title',)}
    list_per_page = 10
from django.contrib import admin
from .models import *

class CategoryTranslationInline(admin.TabularInline):
    model = CategoryTranslation
    extra = 2
    fields = ['language', 'name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","parent"]
    ordering = ["-id",]
    search_fields = ["name"]
    list_filter = ["name"]
    list_per_page = 20
    prepopulated_fields = {"slug": ('name',)}
    inlines = [CategoryTranslationInline]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","slug","category","author","status","created_at"]
    prepopulated_fields = {"slug": ('title',)}
    list_per_page = 10

@admin.register(ArticleTranslation)
class ArticleTranslationAdmin(admin.ModelAdmin):
    list_display = ["id","article","language","title"]
    search_fields = ["title","content"]
    prepopulated_fields = {"slug": ('title',)}

@admin.register(CategoryTranslation)
class CategoryTranslationAdmin(admin.ModelAdmin):
    list_display = ["category", "language", "name"]
    search_fields = ["name"]
    list_filter = ["language"]
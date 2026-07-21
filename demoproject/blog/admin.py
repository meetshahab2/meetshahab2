from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    fields = (
        "title",
        "category",
        "slug",
        "description",
    )
    
    list_display = (
        "id",
        "title",
        "category",
        "slug",
        "created_at",
    )

    search_fields = (
        "title",
        "slug",
    )

    list_filter = (
        "category",
        "created_at",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }
    
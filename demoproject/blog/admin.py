from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    fields = (
        "category",
        "title",
        "slug",
        "cover_image",
        "description",
        "meta_title",
        "meta_description",
        "is_published",
    )

    list_display = (
        "id",
        "title",
        "category",
        "cover_image",
        "is_published",
        "created_at",
    )

    search_fields = (
        "title",
        "slug",
        "meta_title",
    )

    list_filter = (
        "category",
        "is_published",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }
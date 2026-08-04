from django.contrib import admin
from.models import Page,SiteSetting,Menu,ContactMessage

@admin.register(Page)

class PageAdmin(admin.ModelAdmin):

    fields = (
        "title",
        "slug",
        "cover_image",
        "content",
        "meta_title",
        "meta_description",
        "is_published",
    )

    list_display = (
        "id",
        "title",
        "slug",
        "cover_image",
        "is_published",
        "created_at",
    )

    search_fields = (
        "title",
        "slug",
    )

    list_filter = (
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

@admin.register(SiteSetting)

class SiteSettingAdmin(admin.ModelAdmin):

    fields = (
        "site_name",
        "logo",
        "email",
        "phone",
        "address",
    )

    list_display = (
        "id",
        "site_name",
        "email",
        "phone",
    )

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    fields = (
        "title",
        "url",
        "parent",
        "location",
        "order",
        "target_blank",
        "is_active",
    )

    list_display = (
        "id",
        "title",
        "location",
        "url",
        "parent",
        "is_active",
    )

    list_filter = (
        "title",
        "location",
        "is_active",
    )

@admin.register(ContactMessage)
class ContactMessagedmin(admin.ModelAdmin):
    
    list_display = (
        "id",
        "name",
        "phone",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "subject",
    )

    list_filter = (
        "created_at",
    )

    readonly_fields = (
        "name",
        "email",
        "phone",
        "subject",
        "message",
        "created_at",
        "updated_at",
    )
    
# Register your models here.
